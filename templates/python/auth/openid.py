import logging
import os
import urllib3
import webbrowser

from typing import Dict
from urllib.parse import urlencode
from authlib.integrations.base_client import FrameworkIntegration, OAuth2Mixin
from authlib.integrations.requests_client import OAuth2Session

from ..configuration import Configuration
from .base import (
    Authenticator,
    AuthMethod,
    _raise_auth_method_not_supported,
    _soft_deprecate,
)

logger = logging.getLogger(__name__)

ID_TOKEN_FIELD = "id_token"
ACCESS_TOKEN_FIELD = "access_token"


def _get_token(token: Dict[str, str]) -> str:
    if ID_TOKEN_FIELD not in token:
        logger.info(
            f"{ID_TOKEN_FIELD} field couldn't be found in auth token. Falling back to {ACCESS_TOKEN_FIELD}."
        )
        return token[ACCESS_TOKEN_FIELD]

    return token[ID_TOKEN_FIELD]


class OIDCAuthenticator(Authenticator):

    _AuthCodeState = "sd-sdk-state"

    def __init__(self, config: Configuration):
        super().__init__(config)

        if not config.verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if config.oidc_server is None:
            raise ValueError("config.oidc_server is required")
        if config.oidc_client_id is None:
            raise ValueError("config.oidc_client_id is required")

        if config.auth_method in (AuthMethod.CLIENT_CREDENTIALS, AuthMethod.AUTH_CODE):
            if not config.oidc_client_secret:
                raise ValueError(
                    "config.oidc_client_secret is required for "
                    f"{AuthMethod.CLIENT_CREDENTIALS.value}"
                )

        authorize_params = None
        access_token_params = None
        if config.oidc_resource is not None:
            authorize_params = {"resource": config.oidc_resource}
            access_token_params = {"resource": config.oidc_resource}

        server_metadata_url = f"{config.oidc_server}/.well-known/openid-configuration"

        self._app = OAuth2Mixin(
            framework=FrameworkIntegration,
            client_kwargs={"verify": config.verify_ssl},
            client_id=config.oidc_client_id,
            client_secret=config.oidc_client_secret,
            server_metadata_url=server_metadata_url,
            authorize_params=authorize_params,
            access_token_params=access_token_params,
        )
        self._app.client_cls = OAuth2Session
        self._app.load_server_metadata()

    @_soft_deprecate  # type: ignore
    def authenticate(self, username: str = None, password: str = None) -> str:
        if self._config.auth_method == AuthMethod.PASSWORD_GRANT:
            return self._use_password_grant(username, password)
        elif self._config.auth_method == AuthMethod.CLIENT_CREDENTIALS:
            return self._use_client_credentials()
        elif self._config.auth_method == AuthMethod.AUTH_CODE:
            return self._use_authorization_code()

        _raise_auth_method_not_supported(self._config.auth_method)

    def _use_password_grant(self, username: str = None, password: str = None) -> str:
        token = self._app.fetch_access_token(
            username=username or self._config.username,
            password=password or self._config.password,
            scope=self._config.scope,
        )

        return _get_token(token)

    def _use_client_credentials(self):
        token = self._app.fetch_access_token(
            scope=self._config.scope,
            grant_type=AuthMethod.CLIENT_CREDENTIALS.value,
        )

        return _get_token(token)

    def _use_authorization_code(self):
        deploy_callback_url = f"{self._host}/seldon-deploy/auth/callback"

        request_url = self._app.create_authorization_url(
            redirect_uri=deploy_callback_url,
            state=self._AuthCodeState,
            scope=self._config.scope,
        )["url"]

        webbrowser.open_new_tab(request_url)
        print(
            "The following URL should have opened now on a new tab, where you "
            "will be able to log in.\n"
            "If it hasn't, please copy the following URL into a browser.\n"
            "Once you have logged in, you will be redirected and will be shown a code "
            "to copy and paste below."
            f"\n\n\t{request_url}\n\n"
        )
        response_code = self._get_response_code()
        response_code_query = urlencode({"code": response_code})
        response_url = f"{deploy_callback_url}?{response_code_query}"

        token = self._app.fetch_access_token(
            authorization_response=response_url,
            redirect_uri=deploy_callback_url,
            scope=self._config.scope,
        )

        return _get_token(token)

    def _get_response_code(self):
        response_code = None
        while not response_code:
            response_code = input("Please enter your code: ").strip()
        return response_code
