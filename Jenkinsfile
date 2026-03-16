pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            // '--user root' is used here to allow pip to install packages inside the container.
            // This is acceptable in CI/CD pipelines because Docker already isolates
            // the container from the host system.
            // In production environments (e.g. a web server), running as root should be
            // avoided since an attacker who gains access to the container would have
            // full privileges.
            args '--user root'
        }
    }

    environment {
        TARGET_URL = "https://d24moag6y9k9an.cloudfront.net/"
    }

    options {
        timeout(time: 5, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Health Check') {
            steps {
                retry(3) {
                    sh 'python monitor/check_site.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'chmod +x scripts/deploy.sh'
                sh './scripts/deploy.sh'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}