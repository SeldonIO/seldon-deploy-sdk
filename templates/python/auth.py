from urllib3 import Retry
from urllib.parse import urlparse

from seldon_deploy_client.configuration import Configuration
from seldon_deploy_client.rest import RESTClientObject


class SessionAuthenticator:
    """
    Returns the cookie token.
    """

    def __init__(self, config: Configuration):
        self._server = config.host
        self._client = RESTClientObject(config)

        url = urlparse(self._server)
        self._host = f"{url.scheme}://{url.netloc}"

    def authenticate(self, user: str, password: str) -> str:
        auth_path = self._get_auth_path()
        session_cookie = self._submit_auth(auth_path, user, password)
        return session_cookie

    def _get_auth_path(self) -> str:
        # Send unauthenticated request
        res = self._client.GET(self._server)
        return res.urllib3_response.geturl()

    def _submit_auth(self, auth_path: str, user: str, password: str) -> str:
        auth_endpoint = f"{self._host}{auth_path}"
        auth_payload = {"login": user, "password": password}

        res = self._client.pool_manager.request(
            "POST",
            auth_endpoint,
            fields=auth_payload,
            encode_multipart=True,
            retries=Retry(redirect=2, raise_on_redirect=False),
        )

        return res.getheader("set-cookie")
