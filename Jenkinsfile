pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Fateemaaa/assignment01.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t a1_image .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker login'
                sh 'docker tag a1_image fatimazfar/mlops_assignment:first_tag'
                sh 'docker push fatimazfar/mlops_assignment:first_tag'
            }
        }
    }
}