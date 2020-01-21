.PHONY: clean clean-test clean-pyc clean-build help coverage lint test build-container container init
.DEFAULT_GOAL := help

IMAGE_NAME={{ cookiecutter.project_slug }}
DOCKER_COMMON_ARGS=--rm -u $(shell id -u):$(shell id -g) -v $(CURDIR):/workspace -w /workspace $(IMAGE_NAME):latest
RUN=docker run $(DOCKER_COMMON_ARGS)

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

container: build-container ## enter dev mode container
	docker run -it $(DOCKER_COMMON_ARGS) bash

build-container: Dockerfile
	docker build -t $(IMAGE_NAME) --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) $(<D)                       

init: .git/hooks/pre-commit ## initial dev environment
.git/hooks/pre-commit: .pre-commit-config.yaml build-container
	@git init
	@$(RUN) pre-commit install

#############################################	
############## python targets ###############
#############################################	
lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

unittest: ## run tests quickly with the default Python
{%- if cookiecutter.get('use_pytest') == 'y' %}
	pytest
{%- else %}
	python -m unittest discover
{%- endif %}

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.get('use_pytest') == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} -m unittest discover
{%- endif %}
	coverage report -m
	coverage html

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
