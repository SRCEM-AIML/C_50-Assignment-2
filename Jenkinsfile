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
                sh """
                    docker stop ${CONTAINER_NAME} || echo "No running container"
                    docker rm ${CONTAINER_NAME} || echo "No container found"
                    docker rmi ${IMAGE_NAME} || echo "No old image found"
                    docker build -t ${IMAGE_NAME} .
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME} python manage.py test"
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || echo "No running container"
                    docker rm ${CONTAINER_NAME} || echo "No container found"
                    docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}
                """
            }
        }
    }
}
