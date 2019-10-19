
help:						## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
.PHONY: help


init: 		## Installs package requirements
	pip install -r requirements.txt

init-dev:	## Installs package required for development
	pip install -r requirements-test.txt

install:        ## Installs the packages in the current directory
	pip install -e .

test:		## Run unit tests
	python -m unittest 

