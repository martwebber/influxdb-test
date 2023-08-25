pipeline {
    agent any
    environment{
        INFLUXDB_URL = credentials('INFLUXDB_URL')
        INFLUXDB_TOKEN = credentials('INFLUXDB_TOKEN')
        INFLUXDB_BUCKET = credentials('INFLUXDB_BUCKET')
        INFLUXDB_ORG = credentials('INFLUXDB_ORG')
    }
    stages {

              stage('checkout') {
            steps {
checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/martwebber/influxdb-test.git']])
            }
        }
        stage('pip install') {
            steps {
                sh 'pip install -r requirements.txt'

withCredentials([string(credentialsId: 'INFLUXDB_BUCKET', variable: 'INFLUXDB_BUCKET'), string(credentialsId: 'INFLUXDB_TOKEN', variable: 'INFLUXDB_TOKEN'), string(credentialsId: 'INFLUXDB_URL', variable: 'INFLUXDB_URL'), string(credentialsId: 'INFLUXDB_ORG', variable: 'INFLUXDB_ORG')]) {
    sh 'python3 artillery.py'
}
            }
        }
    }
}
