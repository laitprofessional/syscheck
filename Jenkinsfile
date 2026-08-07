pipeline { 
    agent any

    stages {
	stage ('Test') {
	   steps {
	       sh 'pip3 install pytest --user'
   	       sh 'PYTHONPATH=, ~/.local/bin/pytest -v --junitxm=results.xml' 
	   }
	   post {
	       always {
		    junit 'results.xml'
	       }
	   }
        }
     }
}
