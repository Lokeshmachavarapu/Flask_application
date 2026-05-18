pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'git 'https://github.com/Lokeshmachavarapu/Flask_application.git''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-cicd-app'
            }
        }
    }
}
