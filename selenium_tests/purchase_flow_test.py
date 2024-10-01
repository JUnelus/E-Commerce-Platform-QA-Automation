from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()


# Test Case: Purchase Flow Simulation on Sauce Demo
def test_purchase_flow():
    driver.get('https://www.saucedemo.com/')

    # Login first
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(3)  # Wait for login to complete

    # Add a product to the cart
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_button.click()

    # Go to the cart
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    time.sleep(2)  # Wait for the cart page to load

    # Proceed to checkout
    driver.find_element(By.ID, 'checkout').click()

    # Fill in checkout information
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')

    # Continue to the next step
    driver.find_element(By.ID, 'continue').click()

    time.sleep(2)  # Wait for the next page

    # Finish the purchase
    driver.find_element(By.ID, 'finish').click()

    time.sleep(3)  # Wait for the confirmation page to load

    # Validate that the purchase is completed
    assert 'Thank you for your order!' in driver.page_source

    driver.quit()


if __name__ == "__main__":
    test_purchase_flow()
