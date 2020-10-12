.PHONY: install test clean

default: test

install:
	pip install -e .

test:
	PYTHONPATH=./src pytest

clean:
	pip uninstall ngen-v2
