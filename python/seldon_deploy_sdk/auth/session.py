from urllib3 import Retry

from seldon_deploy_sdk.configuration import Configuration
from seldon_deploy_sdk.rest import RESTClientObject

from .base import Authenticator


class SessionAuthenticator(Authenticator):
    """
    Returns the cookie token.
    """

    def __init__(self, config: Configuration,auth_method='password_grant'):
        super().__init__(config,auth_method)

        self._client = RESTClientObject(config)

    def authenticate(self, **kwargs) -> str:

        auth_path = self._get_auth_path()
        if self._auth_method == 'password_grant':
            user = kwargs.get('username', None)
            password = kwargs.get('password', None)
            if user is None:
                user = self._config.username
            if password is None:
                user = self._config.password

            session_cookie = self._submit_auth(auth_path, user, password)
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
