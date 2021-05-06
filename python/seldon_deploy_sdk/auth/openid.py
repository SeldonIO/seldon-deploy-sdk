from authlib.integrations.base_client import FrameworkIntegration, RemoteApp
from authlib.integrations.requests_client import OAuth2Session

from seldon_deploy_sdk.configuration import Configuration

from .base import Authenticator


class OIDCIntegration(FrameworkIntegration):
    oauth2_client_cls = OAuth2Session


class OIDCAuthenticator(Authenticator):
    def __init__(self, config: Configuration,auth_method='password_grant'):
        super().__init__(config,auth_method)

        if config.oidc_server is None:
            raise ValueError("config.oidc_server is required")
        if config.oidc_client_id is None:
            raise ValueError("config.oidc_client_id is required")

        server_metadata_url = f"{config.oidc_server}/.well-known/openid-configuration"
        self._app = RemoteApp(
            framework=OIDCIntegration,
            client_id=config.oidc_client_id,
            client_secret=getattr(config, "oidc_client_secret", None),
            server_metadata_url=server_metadata_url,
        )
        self._app.load_server_metadata()

    def authenticate(self, **kwargs) -> str:

        if self._auth_method == 'password_grant':
            user = kwargs.get('username', None)
            password = kwargs.get('password', None)
            scope = kwargs.get('scope', 'openid profile email groups')

            if user is None:
                user = self._config.username
            if password is None:
                user = self._config.password

            token = self._app.fetch_access_token(
                username=user, password=password, scope=scope
            )
            return token["access_token"]

        raise NotImplementedError("Auth method not specified or not supported")