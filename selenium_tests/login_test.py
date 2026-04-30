from selenium.webdriver.common.by import By
import time

if __package__:
    from .artifact_utils import ArtifactRecorder, build_chrome_driver
else:
    from artifact_utils import ArtifactRecorder, build_chrome_driver


def test_login():
    driver = build_chrome_driver()
    recorder = ArtifactRecorder(test_name='login_test')

    try:
        driver.get('https://www.saucedemo.com/')
        recorder.step(driver, 'open_login_page')

        username = driver.find_element(By.ID, 'user-name')
        password = driver.find_element(By.ID, 'password')
        username.send_keys('standard_user')
        password.send_keys('secret_sauce')
        recorder.step(driver, 'enter_credentials')

        driver.find_element(By.ID, 'login-button').click()
        recorder.step(driver, 'submit_login')

        time.sleep(3)
        recorder.step(driver, 'products_page_loaded')

        assert 'Products' in driver.page_source
    finally:
        recorder.finalize()
        driver.quit()


if __name__ == "__main__":
    test_login()
