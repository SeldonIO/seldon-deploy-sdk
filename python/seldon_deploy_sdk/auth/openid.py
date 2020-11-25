from authlib.integrations.base_client import FrameworkIntegration, RemoteApp
from authlib.integrations.requests_client import OAuth2Session

from seldon_deploy_sdk.configuration import Configuration

from .base import Authenticator


class OIDCIntegration(FrameworkIntegration):
    oauth2_client_cls = OAuth2Session


class OIDCAuthenticator(Authenticator):
    def __init__(self, config: Configuration):
        super().__init__(config)

        # TODO: Check that `config.oidc_server` and `config.oidc_client_id` are
        # set.

        server_metadata_url = f"{config.oidc_server}/.well-known/openid-configuration"
        self._app = RemoteApp(
            framework=OIDCIntegration,
            client_id=config.oidc_client_id,
            client_secret=getattr(config, "oidc_client_secret", None),
            server_metadata_url=server_metadata_url,
        )
        self._app.load_server_metadata()

    def authenticate(self, user: str, password: str) -> str:
        token = self._app.fetch_access_token(
            username=user, password=password, scope="openid"
        )
        return token["access_token"]
