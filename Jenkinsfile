pipeline {
    agent any

    stages {

              stage('checkout') {
            steps {
checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/martwebber/influxdb-test.git']])
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
                withCredentials([string(credentialsId: 'INFLUXDB_BUCKET', variable: 'INFLUXDB_BUCKET')]) {
    sh 'echo $INFLUXDB_BUCKET'
}
            }
        }
    }
}
