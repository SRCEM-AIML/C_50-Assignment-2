pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vedanshgupta25/newa-app-assignment2'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C_50_VedanshGupta_assignment2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop any running container with the same name
                    sh 'docker stop studentproject || true && docker rm studentproject || true'

                    // Run the new container
                    sh 'docker run -d --name studentproject -p 8000:8000 $DOCKER_IMAGE'
                }
            }
        }
    }
}