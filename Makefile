.PHONY: install test clean build

default: test

install: ## Install the package to the active Python's site-packages
	pip install -e .

test: ## Run tests
	PYTHONPATH=./src pytest

clean: ## Remove all build, test, coverage and Python artifacts
	pip uninstall ngen

build: ## Build the package
	python setup.py bdist_wheel

help: ## Show this help
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'
	@echo
