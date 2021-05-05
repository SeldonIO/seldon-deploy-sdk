from urllib.parse import urlparse

from seldon_deploy_sdk.configuration import Configuration


class Authenticator:
    def __init__(self, config: Configuration, auth_method=None):
        self._server = config.host
        self._host = self._get_host()
        self._config = config
        self._auth_method = auth_method

    def authenticate(self, **kwargs) -> str:
        raise NotImplementedError("Authenticate method not implemented")

    def _get_host(self) -> str:
        url = urlparse(self._server)
        return f"{url.scheme}://{url.netloc}"
