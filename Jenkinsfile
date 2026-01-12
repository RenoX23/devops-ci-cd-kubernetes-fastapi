pipeline {
    agent any

    environment {
        IMAGE_NAME = "renowiz/fastapi-devops"
        IMAGE_TAG  = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/RenoX23/devops-ci-cd-kubernetes-fastapi.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Build and push completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
