from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()


# Test Case: Login Test
def test_login():
    driver.get('https://www.saucedemo.com/')

    # Find username and password fields
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')

    # Enter credentials
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')

    # Submit the login form
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(3)  # Wait for the page to load

    # Validate login success
    assert 'Products' in driver.page_source

    driver.quit()


if __name__ == "__main__":
    test_login()
