
pipeline {
    agent any

    environment {
        PLAYWRIGHT_BROWSERS_PATH = "${WORKSPACE}\\ms-playwright"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat '.venv\\Scripts\\python.exe -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v playwrite_sample.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
