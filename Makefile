PACKAGE_NAME := seldon-deploy-client
SWAGGER_CODEGEN_IMAGE := swaggerapi/swagger-codegen-cli:2.4.17
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

python: swagger-v1alpha1.yml templates/python/**/*.py templates/python/*
	rm -rf python/*
	docker run -it --rm \
		-v ${PWD}:/local \
		--user ${CURRENT_UID}:${CURRENT_GID} \
		${SWAGGER_CODEGEN_IMAGE} \
		generate \
		-i /local/swagger-v1alpha1.yml \
		-t /local/templates/python \
		-l python \
		-c /local/config/python.json \
		-o /local/python
	# Add extra files
	cp -r ./templates/python/auth ./python/seldon_deploy_client/auth
	cp -r ./templates/python/dev-requirements.txt ./python/seldon_deploy_client/dev-requirements.txt
