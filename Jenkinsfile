pipeline {
    agent any
    environment {
        IMAGE_NAME = "vedanshgupta25/newa-app-assignment2"
        CONTAINER_NAME = "django-assignment2-container"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C_50_VedanshGupta_assignment2.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME} python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                // Stop and remove existing container if running
                sh 'docker stop ${CONTAINER_NAME} || true && docker rm ${CONTAINER_NAME} || true'

                // Run new container
                sh 'docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}'
            }
        }
    }
}
