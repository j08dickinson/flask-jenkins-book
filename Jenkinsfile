pipeline {
    agent any
    triggers {
    	pollSCM('* * * * *')
    }
    stages {
        stage("Installing dependencies") {
            steps {
                sh "python3 -m venv venv"
		sh '. venv/bin/activate'
		sh 'venv/bin/pip3 install -r chapter5-flask/requirements.txt'
            }
	}
	stage('Starting app') {
	    steps {
		echo 'Starting app...'
		sh 'venv/bin/python chapter5-flask/library.py &'
	    }
	}
	stage('UAT') {
	    steps {
		echo 'Running UAT...'
		sh 'venv/bin/behave chapter5-flask/'
		sh 'pkill -9 -f chapter5-flask/library.py || true'
	    }
        }
    }
}
