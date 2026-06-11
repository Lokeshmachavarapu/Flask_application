pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app"
        DOCKER_TAG = "v1"
        SONAR_PROJECT_KEY = "flask-app"
        SONAR_URL = "http://13.232.160.185:9000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Lokeshmachavarapu/Flask_application.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_URL}
                    """
                }
            }
        }

        stage('Trivy File System Scan') {
            steps {
                sh 'trivy fs . > trivy-report.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        stage('Run Container') {
            steps {
                sh """
                    docker stop flask-container || true
                    docker rm flask-container || true

                    docker run -d \
                    --name flask-container \
                    -p 5000:5000 \
                    ${DOCKER_IMAGE}:${DOCKER_TAG}
                """
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {
                    sh """
                        echo \$PASS | docker login -u \$USER --password-stdin
                        docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} \$USER/${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push \$USER/${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'trivy-report.txt', allowEmptyArchive: true
       }
    }
}
