
pipeline {
  environment {
    registry = "roop1985/python-flask"
    registryCredential = 'docker'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
        when {
                branch 'master'
            }
      steps {
        git 'https://github.com/roopesh2013/flask-app.git'
      }
    }
    stage('Building image') {
        when {
                branch 'master'
            }
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
    stage('Deploy the image using ansible') {
        when {
                branch 'master'
            }
           steps{     
          git credentialsId: 'git-p', url: 'https://github.com/roopesh2013/flask-app'
          ansiblePlaybook extras: '--extra-vars="tag_var=${BUILD_NUMBER}"', installation: 'ansible', playbook: 'docker_manage.yml'  
                    
          }
       }
    }
}
