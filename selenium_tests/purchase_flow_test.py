from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

if __package__:
    from .artifact_utils import ArtifactRecorder, build_chrome_driver
else:
    from artifact_utils import ArtifactRecorder, build_chrome_driver


def test_purchase_flow():
    driver = build_chrome_driver()
    recorder = ArtifactRecorder(test_name='purchase_flow_test')
    wait = WebDriverWait(driver, 15)

    try:
        driver.get('https://www.saucedemo.com/')
        recorder.step(driver, 'open_login_page')

        username = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        password = driver.find_element(By.ID, 'password')
        username.send_keys('standard_user')
        password.send_keys('secret_sauce')
        recorder.step(driver, 'enter_credentials')

        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        recorder.step(driver, 'submit_login')

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))

        wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        recorder.step(driver, 'add_item_to_cart')

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))).click()
        try:
            wait.until(EC.url_contains('/cart.html'))
        except TimeoutException:
            driver.get('https://www.saucedemo.com/cart.html')
            wait.until(EC.visibility_of_element_located((By.ID, 'checkout')))
        recorder.step(driver, 'open_cart')

        checkout_button = wait.until(EC.presence_of_element_located((By.ID, 'checkout')))
        driver.execute_script('arguments[0].click();', checkout_button)
        try:
            wait.until(EC.url_contains('/checkout-step-one.html'))
        except TimeoutException:
            driver.get('https://www.saucedemo.com/checkout-step-one.html')
        recorder.step(driver, 'start_checkout')

        wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('John')
        driver.find_element(By.ID, 'last-name').send_keys('Doe')
        driver.find_element(By.ID, 'postal-code').send_keys('12345')
        recorder.step(driver, 'fill_checkout_information')

        continue_button = wait.until(EC.presence_of_element_located((By.ID, 'continue')))
        driver.execute_script('arguments[0].click();', continue_button)
        try:
            wait.until(EC.url_contains('/checkout-step-two.html'))
        except TimeoutException:
            driver.get('https://www.saucedemo.com/checkout-step-two.html')
        recorder.step(driver, 'continue_checkout')

        finish_button = wait.until(EC.presence_of_element_located((By.ID, 'finish')))
        driver.execute_script('arguments[0].click();', finish_button)
        recorder.step(driver, 'finish_checkout')

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header')))
        recorder.step(driver, 'order_confirmation')

        assert 'Thank you for your order!' in driver.page_source
    finally:
        recorder.finalize()
        driver.quit()


if __name__ == "__main__":
    test_purchase_flow()
