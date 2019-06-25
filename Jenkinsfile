pipeline {
  
  agent { label 'docker' }
  stages {
    stage('build') {
      agent {
        docker {
          // Set both label and image
          label 'docker'
          image 'python:3.7.2'
        }
      }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      agent {
        docker {
          // Set both label and image
          label 'docker'
          image 'python:3.7.2'
        }
      }
      steps {
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
