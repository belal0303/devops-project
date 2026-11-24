pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '123456789012'
        ECR_REPOSITORY = 'devops-web'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        ECR_IMAGE = "${ECR_REGISTRY}/${ECR_REPOSITORY}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-web:${BUILD_NUMBER} .'
            }
        }

        stage('Test Docker Image') {
            steps {
                sh '''
                    docker rm -f devops-test-container || true

                    docker run -d --name devops-test-container -p 5001:5000 devops-web:${BUILD_NUMBER}

                    sleep 5

                    curl -f http://localhost:5001

                    docker rm -f devops-test-container
                '''
            }
        }

        stage('Authenticate to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region ${AWS_REGION} \
                    | docker login --username AWS --password-stdin ${ECR_REGISTRY}
                '''
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh '''
                    docker tag devops-web:${BUILD_NUMBER} ${ECR_IMAGE}:${BUILD_NUMBER}

                    docker tag devops-web:${BUILD_NUMBER} ${ECR_IMAGE}:latest

                    docker push ${ECR_IMAGE}:${BUILD_NUMBER}

                    docker push ${ECR_IMAGE}:latest
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f devops-web-container || true

                    docker pull ${ECR_IMAGE}:${BUILD_NUMBER}

                    docker run -d \
                    --name devops-web-container \
                    -p 5000:5000 \
                    ${ECR_IMAGE}:${BUILD_NUMBER}
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
