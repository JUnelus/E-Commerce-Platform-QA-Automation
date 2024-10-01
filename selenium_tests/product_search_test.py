from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()


# Test Case: Product Search Simulation on Sauce Demo
def test_product_search():
    driver.get('https://www.saucedemo.com/')

    # Login first
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(3)  # Wait for login to complete

    # Simulate searching by validating the product list
    product_title = driver.find_element(By.CLASS_NAME, 'title')

    # Print the product title text to see the actual content
    print(f"Product title text: '{product_title.text}'")

    # Check if the Products page is loaded
    assert product_title.text == 'Products', f"Expected 'Products', but got '{product_title.text}'"

    driver.quit()


if __name__ == "__main__":
    test_product_search()
