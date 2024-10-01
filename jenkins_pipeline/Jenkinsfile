pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/junelus/E-Commerce-Platform-QA-Automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "${PYTHON} -m pip install --upgrade pip"
                sh "${PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Running the login test
                sh "${PYTHON} selenium_tests/login_test.py"

                // Running the product search test
                sh "${PYTHON} selenium_tests/product_search_test.py"

                // Running the purchase flow test
                sh "${PYTHON} selenium_tests/purchase_flow_test.py"
            }
        }

        stage('Publish Test Results') {
            steps {
                // Here you could configure test reports, logs, etc.
                echo "All tests have been executed!"
            }
        }
    }

    post {
        always {
            // Archive any test results or screenshots
            archiveArtifacts artifacts: '**/selenium_tests/screenshots/*.png', allowEmptyArchive: true
        }
    }
}
