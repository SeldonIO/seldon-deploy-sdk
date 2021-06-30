import logging

from authlib.integrations.base_client import FrameworkIntegration, RemoteApp
from authlib.integrations.requests_client import OAuth2Session

from seldon_deploy_sdk.configuration import Configuration

from .base import Authenticator, _soft_deprecate

logger = logging.getLogger(__name__)

IdTokenField = "id_token"


class OIDCIntegration(FrameworkIntegration):
    oauth2_client_cls = OAuth2Session


class OIDCAuthenticator(Authenticator):
    def __init__(self, config: Configuration):
        super().__init__(config)

        if config.oidc_server is None:
            raise ValueError("config.oidc_server is required")
        if config.oidc_client_id is None:
            raise ValueError("config.oidc_client_id is required")

        if config.auth_method == "client_credentials":
            if not config.oidc_client_secret:
                raise ValueError(
                    "config.oidc_client_secret is required for client_credentials"
                )

        access_token_params = None
        if config.oidc_resource is not None:
            access_token_params = {"resource": config.oidc_resource}

        server_metadata_url = f"{config.oidc_server}/.well-known/openid-configuration"

        self._app = RemoteApp(
            framework=OIDCIntegration,
            client_id=config.oidc_client_id,
            client_secret=config.oidc_client_secret,
            server_metadata_url=server_metadata_url,
            access_token_params=access_token_params,
        )
        self._app.load_server_metadata()

    @_soft_deprecate  # type: ignore
    def authenticate(self, username: str = None, password: str = None) -> str:
        if self._config.auth_method == "password_grant":
            token = self._app.fetch_access_token(
                username=username or self._config.username,
                password=password or self._config.password,
                scope=self._config.scope,
            )
            return token[IdTokenField]
        elif self._config.auth_method == "client_credentials":
            token = self._app.fetch_access_token(
                scope=self._config.scope, grant_type="client_credentials"
            )
            return token[IdTokenField]

        raise NotImplementedError("Auth method not specified or not supported")
