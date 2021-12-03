SHELL := /bin/bash
.SHELLFLAGS = -ec
.SILENT:
MAKEFLAGS += --silent
.ONESHELL:
.DEFAULT_GOAL: help

.EXPORT_ALL_VARIABLES:

help:
	echo -e "Please use \`make \033[36m<target>\033[0m\`"
	echo -e "👉\t where \033[36m<target>\033[0m is one of"
	grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS = "(: |##)"}; {printf "• \033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: install  ## install dependencies
install:
	pip install -U pip
	pip install -r requirements.txt

.PHONY: tests
tests: PYTHONPATH=.
tests:
	pytest tests/

.PHONY: lint
lint:
	flake8 --ignore=E501
	safety check --full-report
	bandit day*.py