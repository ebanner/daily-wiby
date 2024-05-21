zip: clean
	zip -r lambda.zip *


venv:
	# 
	# UNTESTED (!)
	#
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt


layer:
	#
	# UNTESTED (!)
	#
	cp -r .venv python
	zip -r python.zip python


clean:
	rm -rf .venv
	rm -rf python python.zip
	rm -rf lambda.zip


unzip:
	unzip lambda.zip -d unzipped

