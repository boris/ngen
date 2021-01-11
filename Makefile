.PHONY: install test clean build

default: test

install:
	pip install -e .

test:
	PYTHONPATH=./src pytest

clean:
	pip uninstall ngen

build:
	python setup.py bdist_wheel
