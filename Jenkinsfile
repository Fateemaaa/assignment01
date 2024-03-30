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
                sh 'docker tag a1_image Fateemaaa/assignment01:first_tag'
                sh 'docker push Fateemaaa/assignment01:first_tag'
            }
        }
    }
}