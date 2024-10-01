from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()


# Test Case: Purchase Flow on Sauce Demo
def test_purchase_flow():
    # Step 1: Go to Sauce Demo login page
    driver.get('https://www.saucedemo.com/')

    # Step 2: Login with standard user credentials
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(3)  # Wait for login to complete

    # Step 3: Add a product to the cart (Sauce Labs Backpack)
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_button.click()

    # Step 4: Navigate to the shopping cart
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    time.sleep(2)  # Wait for the cart page to load

    # Step 5: Proceed to checkout
    driver.find_element(By.ID, 'checkout').click()

    # Step 6: Fill in the checkout information
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')

    # Step 7: Continue to the next step
    driver.find_element(By.ID, 'continue').click()

    time.sleep(2)  # Wait for the next page

    # Step 8: Finish the purchase
    driver.find_element(By.ID, 'finish').click()

    time.sleep(3)  # Wait for the confirmation page to load

    # Step 9: Validate that the purchase was successful
    confirmation_text = driver.find_element(By.CLASS_NAME, 'complete-header').text
    assert confirmation_text == 'Thank you for your order!', f"Expected confirmation message, but got '{confirmation_text}'"

    # Step 10: Close the browser
    driver.quit()


if __name__ == "__main__":
    test_purchase_flow()
