pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Onkar\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        PIP = 'C:\\Users\\Onkar\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '✅ Code pulled from GitHub automatically!'
            }
        }

        stage('Set Up Environment') {
            steps {
                bat '''
                %PYTHON% -m venv venv
                call venv\\Scripts\\activate
                venv\\Scripts\\pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt || echo "No requirements.txt found"
                '''
            }
        }

        stage('Run App') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                venv\\Scripts\\python spotify_voice_eq_player.py
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build Success!'
        }
        failure {
            echo '❌ Build Failed. Check logs.'
        }
    }
}
