pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-web:v2 .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f devops-web-container || true'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker run -d --name devops-web-container -p 5000:5000 devops-web:v2'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
                sh 'curl -f http://localhost:5000'
            }
        }
    }
}
