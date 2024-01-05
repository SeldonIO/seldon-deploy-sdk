.PHONY: install install-dev check-dev licenses test build push-test push

install:
	pip install -e . -r requirements.txt

install-dev:
	pip install -e . -r test-requirements.txt

check-dev:
	@which tox > /dev/null || (echo "Error: tox is not installed. Run `make install-dev` first."; exit 1)

licenses: check-dev
	tox --recreate -e licenses
	cut -d, -f1,3 ./licenses/license_info.csv \
		> ./licenses/license_info.no_versions.csv

test: check-dev
	tox

build:
	python setup.py sdist bdist_wheel

install-package:
	pip install -e .

push-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

push:
	twine upload dist/*
