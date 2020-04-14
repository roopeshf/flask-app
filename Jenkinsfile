
pipeline {
  environment {
    registry = "roop1985/python-flask"
    registryCredential = 'docker repo'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/roopesh2013/flask-app.git'
      }
    }
    stage('Building image') {
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
           steps{      
          git credentialsId: 'git-p', url: 'https://github.com/roopesh2013/flask-app',
          ansiblePlaybook become: true, credentialsId: 'root', disableHostKeyChecking: true, extras: 'tag_var = ${BUILD_NUMBER}', installation: 'ansible', inventory: '/etc/ansible/hosts', limit: 'ansible-node', playbook: 'docker_manage.yml'            
          }

  }
}
