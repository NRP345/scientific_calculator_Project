
pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        DOCKER_IMAGE = 'nrpatil654/scientific-calculator'
        ANSIBLE_INVENTORY = 'inventory'  // Update path as needed
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
        script {
            sh '''
            rm -rf venv  # ✅ Remove broken venv
            python3 -m venv venv  # ✅ Create a new virtual environment
            chmod -R 755 venv  # ✅ Fix permission issues
            
            # ✅ Manually reinstall pip
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            ./venv/bin/python3 get-pip.py
            
            # ✅ Upgrade pip and install dependencies
            ./venv/bin/python3 -m pip install --upgrade pip setuptools
            ./venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt
            '''
        }
    }
}




        stage('Run Unit Tests') {
    steps {
        script {
            try {
                sh './venv/bin/python3 -m unittest test_scientific_calculator'  // ✅ Runs the correct test file
            } catch (Exception e) {
                echo "Unit tests failed. Check logs."
                currentBuild.result = 'FAILURE'
                error("Stopping pipeline due to test failure")
            }
        }
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

