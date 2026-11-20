pipeline {
    agent any

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

        stage('Test Docker Image') {
            steps {
                sh '''
                    docker rm -f devops-test-container || true

                    docker run -d --name devops-test-container -p 5001:5000 devops-web:v2

                    sleep 5

                    curl -f http://localhost:5001

                    docker rm -f devops-test-container
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f devops-web-container || true

                    docker run -d \
                    --name devops-web-container \
                    -p 5000:5000 \
                    devops-web:v2
                '''
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
