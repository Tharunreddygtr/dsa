pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *') // Poll every 5 minutes
    }

    stages {
        stage('Build') {
            when {
                branch 'tharun'
            }
            steps {
                echo 'Building Docker image...'
                script {
                    // Build the Docker image
                    sh 'docker build -t  dsa-python'
                }
            }
        }

        stage('Lint') {
            steps {
                echo 'Running pylint...'
                script {
                    // Run pylint inside the Docker container
                    sh 'docker run --rm dsa-python pylint dsa-python'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest...'
                script {
                    // Run pytest inside the Docker container
                    sh 'docker run --rm dsa-python pytest'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Cleanup Docker containers and images
            sh 'docker system prune -f'
        }
    }
}
