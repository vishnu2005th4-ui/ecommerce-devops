pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/vishnu2005th4-ui/ecommerce-devops'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ecommerce-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5001:5000 ecommerce-app'
            }
        }
    }
}
