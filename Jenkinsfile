pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/YOUR_USERNAME/Spotify_clone.git', branch: 'main'
            }
        }

        stage('Set Up Python') {
            steps {
                echo "Setting up Python virtual environment"
                // Windows command - if on Linux, replace with "sh"
                bat '''
                python -m venv %PYTHON_ENV%
                call %PYTHON_ENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt || echo "No requirements.txt found"
                '''
            }
        }

        stage('Run Script') {
            steps {
                bat '''
                call %PYTHON_ENV%\\Scripts\\activate
                python spotify_voice_eq_player.py || echo "No spotify_voice_eq_player.py file found"
                '''
            }
        }

    }

    post {
        success {
            echo '✅ Build completed successfully!'
        }
        failure {
            echo '❌ Build failed. Check the logs.'
        }
    }
}
