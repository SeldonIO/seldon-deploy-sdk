.PHONY: licenses install-dev test build push-test push

licenses:
	tox --recreate -e licenses
	cut -d, -f1,3 ./licenses/license_info.csv \
		> ./licenses/license_info.no_versions.csv

install-dev:
	pip install -e . -r test-requirements.txt

test:
	tox

build:
	python setup.py sdist bdist_wheel

push-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

push:
	twine upload dist/*
