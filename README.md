# Seldon Deploy SDK

This repository holds different SDK implementations to interact with the Seldon
Deploy API.

> :warning: **NOTE:** The Seldon Deploy SDK only supports Seldon Deploy `>=0.9`.

## Python

### Installation

Since there is no published package yet, to install the Python version of the
SDK you'll need to run:

```bash
pip install 'git+https://github.com/SeldonIO/seldon-deploy-client#egg=seldon-deploy-client&subdirectory=python'
```

Alternatively, you can go into the [`./python`](./python) folder and run:

```bash
pip install -e .
```

### Usage

The Python version of the SDK includes support for sommon common authentication
workflows.

> :warning: **NOTE:** The SDK currently only supports the authentication flow
> using cookies and Dex.

You can see an example usage below:

```python
from seldon_deploy_client import EnvironmentApi, Configuration, ApiClient
from seldon_deploy_client.auth import OIDCAuthenticator

config = Configuration()
config.host = "http://188.166.139.135/seldon-deploy/api/v1alpha1"
config.oidc_client_id = "deploy-server"
config.oidc_server = "http://188.166.139.135/auth/realms/deploy-realm"

auth = OIDCAuthenticator(config)
config.access_token = auth.authenticate("admin@seldon.io", "12341234")

api_client = ApiClient(config)

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
