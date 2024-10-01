# Test Plan for E-Commerce Platform QA Automation

## Scope
This project aims to automate the testing of critical user flows in an e-commerce platform:
- User login
- Product search
- Add product to cart
- Checkout

## Test Cases

### 1. **Login Test**
- **Description**: Verify login functionality with valid and invalid credentials.
- **Test Type**: Automated (Selenium)
- **Expected Outcome**: User should be able to log in with valid credentials.

### 2. **Product Search Test**
- **Description**: Verify search functionality for products.
- **Test Type**: Automated (Selenium)
- **Expected Outcome**: Search results should display relevant products.

### 3. **Add to Cart Test**
- **Description**: Verify that products can be added to the cart.
- **Test Type**: Automated (Selenium)
- **Expected Outcome**: Product should be successfully added to the cart.

### 4. **Checkout Test**
- **Description**: Validate the checkout process.
- **Test Type**: Automated (Selenium), API (Postman), SQL (Database Validation)
- **Expected Outcome**: Purchase should be completed, and database should reflect inventory changes.

