from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path
from typing import List

import imageio.v2 as imageio
import numpy as np
from selenium import webdriver

_ARTIFACT_ROOT = Path(__file__).resolve().parents[1] / 'artifacts'


def _slugify(value: str) -> str:
    sanitized = re.sub(r'[^a-zA-Z0-9_-]+', '_', value.strip().lower())
    return sanitized.strip('_') or 'step'


def build_chrome_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1440,900')

    if os.getenv('HEADLESS', 'false').lower() in {'1', 'true', 'yes'}:
        options.add_argument('--headless=new')

    return webdriver.Chrome(options=options)


class ArtifactRecorder:
    def __init__(self, test_name: str, fps: int = 1) -> None:
        self.test_name = _slugify(test_name)
        self.fps = fps
        self._step_index = 1
        self._frames: List[Path] = []

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.run_dir = _ARTIFACT_ROOT / self.test_name / timestamp
        self.screenshots_dir = self.run_dir / 'screenshots'
        self.video_dir = self.run_dir / 'video'
        self.screenshots_dir.mkdir(parents=True, exist_ok=True)
        self.video_dir.mkdir(parents=True, exist_ok=True)

    def step(self, driver: webdriver.Chrome, action_name: str) -> Path:
        filename = f"{self._step_index:02d}_{_slugify(action_name)}.png"
        screenshot_path = self.screenshots_dir / filename
        driver.save_screenshot(str(screenshot_path))

        self._frames.append(screenshot_path)
        self._step_index += 1
        return screenshot_path

    def finalize(self) -> Path | None:
        if not self._frames:
            return None

        video_path = self.video_dir / f'{self.test_name}.mp4'
        try:
            target_height, target_width = self._resolve_target_size()
            with imageio.get_writer(
                str(video_path),
                fps=self.fps,
                codec='libx264',
                macro_block_size=1,
                ffmpeg_log_level='error',
            ) as writer:
                for frame_path in self._frames:
                    frame = imageio.imread(frame_path)
                    writer.append_data(self._normalize_frame(frame, target_height, target_width))
        except Exception as exc:
            # Keep UI failure signal clear even if ffmpeg fails.
            print(f'[artifact] Video generation skipped: {exc}')
            return None

        return video_path

    def _resolve_target_size(self) -> tuple[int, int]:
        first_frame = imageio.imread(self._frames[0])
        height, width = first_frame.shape[:2]

        # libx264 with yuv420p requires even dimensions.
        target_height = max(2, height - (height % 2))
        target_width = max(2, width - (width % 2))
        return target_height, target_width

    @staticmethod
    def _normalize_frame(frame: np.ndarray, target_height: int, target_width: int) -> np.ndarray:
        if frame.ndim == 2:
            frame = np.stack([frame, frame, frame], axis=-1)
        elif frame.ndim == 3 and frame.shape[2] > 3:
            frame = frame[:, :, :3]

        height, width = frame.shape[:2]
        crop_height = min(height, target_height)
        crop_width = min(width, target_width)
        normalized = frame[:crop_height, :crop_width]

        if crop_height == target_height and crop_width == target_width:
            return normalized

        canvas = np.zeros((target_height, target_width, 3), dtype=normalized.dtype)
        canvas[:crop_height, :crop_width] = normalized
        return canvas


