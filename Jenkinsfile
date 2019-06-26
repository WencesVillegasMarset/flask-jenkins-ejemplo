pipeline {
  agent none
  stages {
    stage('build') {
      agent {
        docker {
          // Set both label and image
          image 'python:3.7.2'
          args '--user 0:0'
        }
      }
      steps {
        sh 'pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      agent {
        docker {
          // Set both label and image
          image 'python:3.7.2'
          args '--user 0:0'
        }
      }
      steps {
        sh 'pip install -r requirements.txt --user'
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
