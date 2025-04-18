pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📥 Cloning GitHub repository...'
                checkout scm
            }
        }

        stage('Set Up Python Env') {
            steps {
                echo '🐍 Setting up virtual environment...'
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script') {
            steps {
                echo '▶️ Running main Python script...'
                sh '''
                    source $VENV_DIR/bin/activate
                    python3 spotify_voice_eq_player.py
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and run successful!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
