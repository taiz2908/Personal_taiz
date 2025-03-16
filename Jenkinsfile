pipeline {
    agent any
    options {
    buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
  }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Hello2') {
            steps {
                echo 'Hello World2'
            }
        }
        stage('Hello3') {
            steps {
                echo 'Hello World3'
            }
        }
        stage('Hello4') {
            steps {
                echo 'Hello World4'
            }
        }
    }
    post{
        cleanup {
            cleanWs()
        }
    }
}