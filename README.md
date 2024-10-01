# E-Commerce Platform QA Automation

This repository contains automated tests for the **E-Commerce Platform**, covering UI testing with Selenium, API testing using Postman, and CI/CD integration with Jenkins. The tests are designed to validate the core functionalities of an e-commerce platform, such as user login, product search, and purchase flow.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running Tests](#running-tests)
  - [UI Tests with Selenium](#ui-tests-with-selenium)
  - [API Tests with Postman](#api-tests-with-postman)
- [Continuous Integration (CI) with Jenkins](#continuous-integration-ci-with-jenkins)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

---

## Project Structure

```bash
├── jenkins_pipeline/          # Contains Jenkinsfile for CI/CD
├── postman_tests/             # Contains Postman API collections
│   └── product_api_tests.postman_collection.json
├── requirements.txt           # Python dependencies for Selenium tests
├── selenium_tests/            # Selenium UI tests
│   ├── login_test.py
│   ├── product_search_test.py
│   ├── purchase_flow_test.py
│   └── screenshots/           # Directory where screenshots will be saved
├── sql_queries/               # SQL scripts for validating database
│   └── validate_purchase.sql
└── mentoring_docs/            # Documentation for QA best practices
    └── qa_best_practices.md
```
## Requirements
Ensure you have the following installed on your local machine or Jenkins server:

- Python 3.7+
- Google Chrome (or any browser you want to automate)
- ChromeDriver (compatible with the installed Chrome version)
- Jenkins (for CI/CD)
- Postman (for API testing)

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/junelus/E-Commerce-Platform-QA-Automation.git
    cd E-Commerce-Platform-QA-Automation
    ```

2. **Set Up Python Environment:**
    Install Python dependencies:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
    Install ChromeDriver for Selenium (automatically handled by `chromedriver-autoinstaller`).

3. **Verify Python Installation:**
    Ensure Python and pip are installed correctly:
    ```bash
    python --version
    pip --version
    ```

## Running Tests

### UI Tests with Selenium
You can run the Selenium tests using Python. The tests include:

- Login functionality (`login_test.py`)
- Product search functionality (`product_search_test.py`)
- Purchase flow functionality (`purchase_flow_test.py`)

#### Running UI Tests

**Login Test:**
```bash
python selenium_tests/login_test.py
```
Product Search Test:

```bash
python selenium_tests/product_search_test.py
```
### Purchase Flow Test:

```bash
python selenium_tests/purchase_flow_test.py
```
### API Tests with Postman
You can run the API tests using Postman or Newman (the command-line runner for Postman).

Import the Postman collection from the postman_tests/ directory:

File → Import → Select product_api_tests.postman_collection.json
Run the collection within Postman, or use Newman to run from the command line:

```bash
newman run postman_tests/product_api_tests.postman_collection.json
```
### Continuous Integration (CI) with Jenkins
The project is configured for continuous integration with Jenkins. The Jenkinsfile defines the pipeline stages for running the tests.

#### Jenkinsfile Overview
- Checkout Code: Pulls the latest code from the repository.
- Install Dependencies: Installs the required Python dependencies using pip.
- Run Selenium Tests: Executes the Selenium UI tests.
- Publish Artifacts: Archives any screenshots taken during the test runs.

#### Jenkins Setup Instructions
- Install Python on the Jenkins server.
- Add Python and ChromeDriver to the system's PATH.
- Configure a Jenkins pipeline using the provided Jenkinsfile.

#### Running the Jenkins Pipeline
- Go to your Jenkins dashboard, create a new pipeline, and point it to this repository.
- Trigger a build by clicking Build Now in Jenkins.

#### Artifacts
Any screenshots taken during failed tests will be archived in the `selenium_tests/screenshots/` directory. These screenshots will be uploaded as artifacts in Jenkins for review.

### Best Practices
Follow QA Automation Best Practices for:

- Writing modular and maintainable test code.
- Using the Page Object Model (POM) for UI testing.
- Managing test data and configurations efficiently.
- Integrating automated tests with CI/CD pipelines like Jenkins.

### Contributing
- Fork the repository.
- Create a feature branch (`git checkout -b feature/your-feature-name`).
- Commit your changes (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature/your-feature-name`).
- Create a new Pull Request.


### Key Sections in the `README.md`:

1. **Project Structure**: Describes the directory layout of the project, helping new contributors and users understand how the project is organized.
   
2. **Requirements**: Lists the necessary software and tools needed to run the tests.

3. **Installation**: Provides step-by-step instructions to install Python dependencies and set up the environment.

4. **Running Tests**:
   - Explains how to run the Selenium UI tests individually.
   - Shows how to run API tests using Postman or Newman.

5. **CI Integration**:
   - Describes how to set up Jenkins with the provided `Jenkinsfile` and run automated builds.
   - Explains how Jenkins archives screenshots as artifacts.

6. **Best Practices**: Links to the `qa_best_practices.md` document, which covers important guidelines for writing and managing QA automation tests.

7. **Contributing**: Provides instructions for contributing to the project, ensuring that collaboration is smooth.

---

### Additional Notes:
- This `README.md` is formatted to follow best practices for clarity and completeness, making it easy for other developers and QA engineers to follow.
- The links within the document will automatically reference the correct files when placed in the root directory of your project.

Let me know if you need further adjustments or details!