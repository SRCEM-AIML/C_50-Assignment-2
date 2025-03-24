pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vedanshgupta/shopping-app:latest'  // Replace with your Docker Hub repo
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C_50-Assignment-2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    bat 'docker login -u "your-docker-username" -p "your-docker-password"'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    bat 'docker push %DOCKER_IMAGE%'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker run -d -p 8000:8000 --name shopping-app %DOCKER_IMAGE%'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
