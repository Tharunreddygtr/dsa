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
                echo 'Building...'
                // Add build steps, e.g., linting, tests, etc.
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // Add test steps
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any cleanup steps
        }
    }
}
