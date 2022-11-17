pipeline {
	agent any
	stages {
		stage ('Checkout') {
			steps {
				git branch:'master', url: 'https://github.com/2000726/quiz.git'
			}
		}
		stage('Build') {
			agent {
				docker {
					image 'python:3.11.0-slim-buster'
					reuseNode tru
				}
			}
			steps {
				sh 'pip install -r src/requirements.txt'
			}
		}
		stage('Code Quality Check via SonarQube') {
			steps {
				script {
					def scannerHome = tool 'SonarQube';
						withSonarQubeEnv('SonarQube') {
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=QUIZ -Dsonar.sources=."
						}
					}
				}
			}
		}
	post {
		always {
			recordIssues enabledForFailure: true, tool: sonarQube()
		}
	}
}