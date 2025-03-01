
pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        DOCKER_IMAGE = 'nrpatil654/scientific-calculator'
        ANSIBLE_INVENTORY = '/etc/ansible/hosts'  // Update path as needed
        ANSIBLE_PLAYBOOK = 'deploy.yml'  // Name of your Ansible playbook
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/NRP345/scientific_calculator_Project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'   // Create virtual environment
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'source venv/bin/activate && python3 -m unittest discover -s tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i $ANSIBLE_INVENTORY $ANSIBLE_PLAYBOOK'
            }
        }
    }
}
