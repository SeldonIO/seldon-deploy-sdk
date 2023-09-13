.PHONY: install-dev check-dev licenses test build push-test push

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

#requires pip install wheel
build:
	python setup.py sdist bdist_wheel

push-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

push:
	twine upload dist/*
