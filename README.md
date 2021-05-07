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
config.oidc_server = "http://X.X.X.X/auth/realms/deploy-realm"
config.username = "*******"
config.password = "*******"
config.auth_method = 'password_grant'

auth = OIDCAuthenticator(config)
config.access_token = auth.authenticate()

api_client = ApiClient(config, auth)

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
make python
```

### Templates

There is some custom logic added on top of each client.
These extra files and customisation can be found in the
[`./templates`](./templates) folder.
