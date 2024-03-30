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

    }
}