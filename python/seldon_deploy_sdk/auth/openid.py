from authlib.integrations.base_client import FrameworkIntegration, RemoteApp
from authlib.integrations.requests_client import OAuth2Session

from seldon_deploy_sdk.configuration import Configuration

from .base import Authenticator


class OIDCIntegration(FrameworkIntegration):
    oauth2_client_cls = OAuth2Session


class OIDCAuthenticator(Authenticator):
    def __init__(self, config: Configuration):
        super().__init__(config)

        if config.oidc_server is None:
            raise ValueError("config.oidc_server is required")
        if config.oidc_client_id is None:
            raise ValueError("config.oidc_client_id is required")

        if config.auth_method == 'password_grant':
            if not config.username:
                raise ValueError("config.username is required for password_grant")
            if not config.password:
                raise ValueError("config.password is required for password_grant")

        server_metadata_url = f"{config.oidc_server}/.well-known/openid-configuration"
        self._app = RemoteApp(
            framework=OIDCIntegration,
            client_id=config.oidc_client_id,
            client_secret=getattr(config, "oidc_client_secret", None),
            server_metadata_url=server_metadata_url,
        )
        self._app.load_server_metadata()

    def authenticate(self) -> str:

        if self._config.auth_method == 'password_grant':

            token = self._app.fetch_access_token(
                username=self._config.username, password=self._config.password, scope=self._config.scope
            )
            return token["access_token"]
        elif self._auth_method == 'client_credentials':
            raise NotImplementedError("Client credentials flow not yet supported")

        raise NotImplementedError("Auth method not specified or not supported")