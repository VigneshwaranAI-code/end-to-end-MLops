pipeline{
    agent any 

    stages{
        stage('clone githun repo to jenkins'){
            steps{
                script{
                    echo 'clone github repo to jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/VigneshwaranAI-code/end-to-end-MLops.git']])
                }
            }
        }
    }
}