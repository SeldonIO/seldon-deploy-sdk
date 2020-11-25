.PHONY: licenses install-dev

licenses:
	tox --recreate -e licenses
	cut -d, -f1,3 ./licenses/license_info.csv \
		> ./licenses/license_info.no_versions.csv

install-dev:
	pip install -e . -r test-requirements.txt
