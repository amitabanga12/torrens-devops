pipeline {
    agent {
        docker {
            image "python:alpine"
            args "--user root --privileged"
        }
    }

    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('set-up') {
            steps {
                sh 'python3 -m venv python_venv'
                sh 'source python_venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python devops-assessment-2/manage.py jenkins --enable-coverage ./devops-assessment-2/'
            }
            post {
                always {
                    junit skipPublishingChecks: true, testResults: 'reports/junit.xml'
                }
            }
        }
    }
}