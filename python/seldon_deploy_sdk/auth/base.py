from urllib.parse import urlparse

from seldon_deploy_sdk.configuration import Configuration


class Authenticator:
    def __init__(self, config: Configuration):
        self._server = config.host
        self._host = self._get_host()
        self._config = config

    def authenticate(self) -> str:
        raise NotImplementedError("Authenticate method not implemented")

    def _get_host(self) -> str:
        url = urlparse(self._server)
        return f"{url.scheme}://{url.netloc}"
