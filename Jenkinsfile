pipeline {
	agent any
	stages {
		stage ('Checkout') {
			steps {
				git branch:'master', url: 'https://github.com/OWASP/Vulnerable-Web-Application.git'
			}
		}
		stage('Code Quality Check via SonarQube') {
			steps {
				script {
					def scannerHome = tool '<change to SonarQube Name>';
						withSonarQubeEnv('<above>') {
						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=<sonarqube project name> -Dsonar.sources=."
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