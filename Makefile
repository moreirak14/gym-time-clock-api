.PHONY: help setup requirements lint pre-commit copy-envs clean test report run-local run-docker

PROJECT_NAME := gym-time-clock-api

help: ## Show help.
	@printf "A set of development commands.\n"
	@printf "\nUsage:\n"
	@printf "\t make \033[36m<commands>\033[0m\n"
	@printf "\nThe Commands are:\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Setup poetry environment
	poetry shell
	poetry install

requirements: ## Export requirements file based on poetry packages
	poetry export -f requirements.txt --output requirements.txt --without-hashes

lint | pre-commit: ## Run the pre-commit config
	poetry run pre-commit run -a

copy-envs: ## Create secret file
	@cp -n .example.secrets.toml .secrets.toml

clean: ## Clean up
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .coverage
	rm -rf  coverage_html
	rm -rf .pytest_cache
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf celerybeat-schedule
	rm -rf *.pyc
	rm -rf *__pycache__

test: ## Run tests locally
	poetry run pytest --cov=src --color=yes tests/

report: test ## Create test report
	pytest --cov-report html:./htmlcov

migration-local: ## Database migration locally
	poetry run alembic revision --autogenerate -m '$(filter-out $@,$(MAKECMDGOALS))'

migrate-local: ## Database migrate locally
	poetry run alembic upgrade head
	poetry run alembic stamp head

run-local: ## Run server locally
	python main.py

run-docker: ## Run server on docker instance
	docker-compose up -d
