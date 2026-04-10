pipeline {
    agent any

    environment {
        GCP_PROJECT = "mlops-492602"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        IMAGE_NAME = "ml-project"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning repo...'
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/VigneshwaranAI-code/end-to-end-MLops.git'
                    ]]
                )
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                pip install --upgrade pip
                pip install -e .
                '''
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training model...'
                sh 'python pipeline/training_pipeline.py'
            }
        }


        stage('Build & Push Docker Image') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}

                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}
                    gcloud auth configure-docker --quiet

                    docker build -t gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:${IMAGE_TAG} .
                    docker push gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }
}