pipeline {
    agent any

    environment {
       PLAYWRIGHT_BROWSERS_PATH = "${WORKSPACE}\\ms-playwright"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '"%PYTHON%" -m pytest "playwright_sample.py" -v'
            }
        }
    }

    post {
        always {
            echo 'Playwright test execution completed.'
        }
    }
}
