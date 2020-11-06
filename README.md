# Seldon Deploy SDK

This repository holds different SDK implementations to interact with the Seldon
Deploy API.

> :warning: The Seldon Deploy SDK only supports Seldon Deploy `>=0.9`.

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
from seldonDeploymentResponse.auth import SessionAuthenticator

config = Configuration()
config.host = "http://157.245.28.216/seldon-deploy/api/v1alpha1"

auth = SessionAuthenticator(confg)
session_cookie = auth.authenticate("******", "*******")

api_client = ApiClient(confg, cookie=session_cookie)

env_api = EnvironmentApi(api_client)
user = env_api.read_user()

print(user)
```

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
