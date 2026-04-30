from selenium.webdriver.common.by import By
import time

if __package__:
    from .artifact_utils import ArtifactRecorder, build_chrome_driver
else:
    from artifact_utils import ArtifactRecorder, build_chrome_driver


def test_product_search():
    driver = build_chrome_driver()
    recorder = ArtifactRecorder(test_name='product_search_test')

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
        product_title = driver.find_element(By.CLASS_NAME, 'title')
        recorder.step(driver, 'open_products_page')

        print(f"Product title text: '{product_title.text}'")
        assert product_title.text == 'Products', f"Expected 'Products', but got '{product_title.text}'"
    finally:
        recorder.finalize()
        driver.quit()


if __name__ == "__main__":
    test_product_search()
