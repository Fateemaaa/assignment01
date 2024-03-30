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
                bat 'docker build -t a1_image .'
            }
        }

        stage('Pubat to Docker Hub') {
            steps {
                bat 'docker login'
                bat 'docker tag a1_image Fateemaaa/assignment01:first_tag'
                bat 'docker push Fateemaaa/assignment01:first_tag'
            }
        }
    }
}