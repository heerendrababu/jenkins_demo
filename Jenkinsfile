
pipeline {
    agent any

    environment {
        PLAYWRIGHT_BROWSERS_PATH = 'C:\\tools\\ms-playwright'
        PYTHON = 'C:\\Users\\udayc\\PycharmProjects\\PythonProject2\\my_env\\Scripts\\python.exe'
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

