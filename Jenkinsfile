pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vedanshgupta25/newa-app-assignment2"
        DOCKER_CREDENTIALS_ID = "vedansggupta25"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo "Pulling latest code from Git repository..."
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    echo "Logging into Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    echo "Running new container from Docker Hub image..."
                    sh "docker run -d -p 8000:8000 ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
