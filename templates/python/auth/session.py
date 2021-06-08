from urllib3 import Retry

from seldon_deploy_sdk.configuration import Configuration
from seldon_deploy_sdk.rest import RESTClientObject

from .base import Authenticator, _soft_deprecate


class SessionAuthenticator(Authenticator):
    """
    Returns the cookie token.
    """

    def __init__(self, config: Configuration):
        super().__init__(config)

        self._client = RESTClientObject(config)

    @_soft_deprecate  # type: ignore
    def authenticate(self, username: str = None, password: str = None) -> str:
        auth_path = self._get_auth_path()
        if self._config.auth_method == "password_grant":
            session_cookie = self._submit_auth(
                auth_path,
                username or self._config.username,
                password or self._config.password,
            )
            return session_cookie

        raise NotImplementedError("Auth method not specified or not supported")

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
