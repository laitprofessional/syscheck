pipeline { 
    agent any

    stages {
	stage ('Test') {
	   steps {
	       sh 'pip3 install pytest --user --break-system-packages'
   	       sh 'PYTHONPATH=. python3 -m  pytest -v --junitxml=results.xml' 
	   }
	   post {
	       always {
		    junit 'results.xml'
	       }
	   }
        }
     }
}
