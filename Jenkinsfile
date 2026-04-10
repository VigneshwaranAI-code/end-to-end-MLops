pipeline{
    agent any 

    environment {
        VENV_DIR ='venv'
        GCP_PORJECT = "mlops-492602"
        GCLOUD_PATH = "/var/jenkins_home/google-cloude-sdk/bin"
    }

    stages{
        stage('clone githun repo to jenkins'){
            steps{
                script{
                    echo 'clone github repo to jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/VigneshwaranAI-code/end-to-end-MLops.git']])
                }
            }
        }

        stage('setting up our Virtual Environment and Installing dependancies'){
            steps{
                script{
                    echo 'setting up our Virtual Environment and Installing dependancies'
                    sh '''
                    python -m venv venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

         stage('Building and Pushing Docker Image to GCR '){
            steps{
                with credentials([file(credentialsId :'gcp-key', variable : "GOOGLE_APPLICATION_CREDENTIALS")]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR............'
                        sh '''
                        export PATH=$PATH:$(GCLOUDE_PATH)

                        gcloud auth activate-service account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        
                        gcloud config set project ${GCP_PROJECT}


                        gcloud auth configure-docker --quiet 

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push -t gcr.io/${GCP_PROJECT}/ml-project:latest 
                        '''
                    }
                }
            }
        }
    }
}