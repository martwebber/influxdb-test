pipeline {
    agent any

    stages {
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
