.PHONY: install test

default: test

install:
	pip install -e .

test:
	PYTHONPATH=./src pytest
