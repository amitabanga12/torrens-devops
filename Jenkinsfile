pipeline {
    agent {
        docker {
            image "python:3.11.0-bullseye"
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
                sh 'python3 -m venv venv'
                sh 'sh ./venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python devops-a2/devops_project/manage.py jenkins --enable-coverage ./devops-a2/devops_project/'
            }
            post {
                always {
                    junit skipPublishingChecks: true, testResults: 'reports/junit.xml'
                }
            }
        }
    }
}