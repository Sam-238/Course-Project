pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/Sam-238/Course-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-registration .'
            }
        }
    }
}