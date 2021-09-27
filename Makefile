SWAGGER_CODEGEN_IMAGE := swaggerapi/swagger-codegen-cli:2.4.17
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

.PHONY: python

python:
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
		--additional-properties 'infoEmail=hello@seldon.io' \
		--git-user-id 'SeldonIO' \
		--git-repo-id 'seldon-deploy-sdk' \
		-o /local/python
	# Add extra files
	cp -r ./templates/python/auth ./python/seldon_deploy_sdk/auth
	cp -r ./templates/python/Makefile ./python/Makefile
	# Generate licenses
	mkdir python/licenses
	make -C python licenses
	# Apply patch
	git apply templates/python/metadata_tags_metrics.patch
