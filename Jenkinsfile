pipeline {
    agent any

    environment {
        IMAGE_NAME = "vedanshgupta25/newa-app-assignment2"
        CONTAINER_NAME = "ef293c0ca45dd2338080a4f0e20a8bf20589f6dd8a8119412934bde8647527a8"
        DOCKER_PATH = '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe"'
    }

    stages {
        stage('Check Docker') {
            steps {
                script {
                    sh "${DOCKER_PATH} --version"
                }
            }
        }
        
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SRCEM-AIML/C_50_VedanshGupta_assignment2.git'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    sh """
                        ${DOCKER_PATH} stop ${CONTAINER_NAME} || echo "No running container"
                        ${DOCKER_PATH} rm ${CONTAINER_NAME} || echo "No container found"
                        ${DOCKER_PATH} rmi ${IMAGE_NAME} || echo "No old image found"
                        ${DOCKER_PATH} build -t ${IMAGE_NAME} .
                    """
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh "${DOCKER_PATH} run --rm ${IMAGE_NAME} python manage.py test"
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh """
                            echo "$DOCKER_PASS" | ${DOCKER_PATH} login -u "$DOCKER_USER" --password-stdin
                            ${DOCKER_PATH} push ${IMAGE_NAME}
                        """
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh """
                        ${DOCKER_PATH} stop ${CONTAINER_NAME} || echo "No running container"
                        ${DOCKER_PATH} rm ${CONTAINER_NAME} || echo "No container found"
                        ${DOCKER_PATH} run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}
                    """
                }
            }
        }
    }
}
