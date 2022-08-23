# Seldon Deploy SDK

This repository holds different SDK implementations to interact with the Seldon
Deploy API.

> :warning: **NOTE:** The Seldon Deploy SDK only supports Seldon Deploy `>=0.9`.

## Python

### Installation

To install the Python version of the SDK run:

```bash
pip install seldon-deploy-sdk
```

### Usage

The Python version of the SDK includes support for common authentication workflows.

You can see an example usage below:

```python
from seldon_deploy_sdk import EnvironmentApi, Configuration, ApiClient
from seldon_deploy_sdk.auth import OIDCAuthenticator

config = Configuration()
config.host = "http://X.X.X.X/seldon-deploy/api/v1alpha1"
config.oidc_client_id = "sd-api"
config.oidc_client_secret = "sd-api-secret"
config.oidc_server = "http://X.X.X.X/auth/realms/deploy-realm"
config.auth_method = "auth_code"

auth = OIDCAuthenticator(config)
config.id_token = auth.authenticate()

api_client = ApiClient(configuration=config, authenticator=auth)

env_api = EnvironmentApi(api_client)
user = env_api.read_user()

print(user)
```

You can find more details on the [Python SDK
documentation](./python/README.md).

## SDK Generation

To generate a new version of the SDK, you can use the `Makefile` targets
available.
For example, for Python you could do:

```bash
make -C python install-dev

make python
```

### Templates

There is some custom logic added on top of each client.
These extra files and customisation can be found in the
[`./templates`](./templates) folder.

For Seldon Deploy model metadata service, we are having to patch two additional dict type parameters namely `tags` and `metrics` to the generated docs and sdk code. We do this manually, using the same make command, by applying the [patch file](./templates/python/metadata_tags_metrics.patch) file to the code, post sdk generation task. In some cases the patch apply cmd may fail, and there might be a requirement to re-generate the patch manually by changing the generated docs/sdk files as required.

### How to create a new release?

1. Update the [swagger file](./swagger-v1alpha1.yml) with latest specification.
2. Update [config file](./config/python.json) to bump the package version.
3. Run `make python` to re-generate the sdk api files from new specifications. If you get error `error: patch failed` then update the template customisation [patch file](./templates/python/metadata_tags_metrics.patch). See templates section above for more details.

4. Run `make -C build push` to build & push latest release to [PyPi](https://pypi.org/project/seldon-deploy-sdk/)
5. Create a new Github Tag and Release with latest version and notes.
