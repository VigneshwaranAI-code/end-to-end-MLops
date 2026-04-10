pipeline{
    agent any 

    environment {
        VENV_DIR ='venv'
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
    }
}