pipeline {
    agent any

    environment {
        IMAGE_NAME = "vedanshgupta25/newa-app-assignment2"
        CONTAINER_NAME = "django-assignment2-container"
    }

    stages {
        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }
        
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C_50_VedanshGupta_assignment2.git'
            }
        }
        
        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        
        stage('Run Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME} python manage.py test"
            }
        }
        
        stage('Deploy') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || echo "Container not running"
                    docker rm ${CONTAINER_NAME} || echo "Container not found"
                    docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}
                """
            }
        }
    }
}
