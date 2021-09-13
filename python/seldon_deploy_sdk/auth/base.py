import logging
from enum import auto, Enum
from functools import wraps

from urllib.parse import urlparse
from typing import Callable, Optional

from seldon_deploy_sdk.configuration import Configuration

logger = logging.getLogger(__name__)


def _deprecation_warning(field: str):
    logger.warning(
        "DEPRECATED!! "
        f"Future versions of seldon_deploy_sdk will require that the {field} "
        f"field is set in the Configuration object (under config.{field}). "
        f"Subsequently, the authenticate() method won't accept a {field} "
        "parameter anymore."
    )


def _soft_deprecate(
    authenticate: Callable[["Authenticator", Optional[str], Optional[str]], str]
):
    @wraps(authenticate)
    def _f(self, username: str = None, password: str = None) -> str:
        if self._config.auth_method == AuthMethod.PASSWORD_GRANT:
            if username:
                _deprecation_warning("username")
            elif not self._config.username:
                raise ValueError(
                    "config.username is required for "
                    f"{AuthMethod.PASSWORD_GRANT.name}"
                )

            if password:
                _deprecation_warning("password")
            elif not self._config.password:
                raise ValueError(
                    "config.password is required for "
                    f"{AuthMethod.PASSWORD_GRANT.name}"
                )

        return authenticate(self, username, password)

    return _f


class AuthMethod(Enum):
    PASSWORD_GRANT = auto()
    CLIENT_CREDENTIALS = auto()
    AUTH_CODE = auto()


class Authenticator:
    def __init__(self, config: Configuration):
        self._server = config.host
        self._host = self._get_host()
        self._config = config

        if self._config.auth_method == AuthMethod.PASSWORD_GRANT:
            if not self._config.username:
                _deprecation_warning("username")
                #  raise ValueError(f"config.username is required for {AuthMethod.PASSWORD_GRANT.name}")

            if not self._config.password:
                _deprecation_warning("password")
                #  raise ValueError(f"config.username is required for {AuthMethod.PASSWORD_GRANT.name}")

    def authenticate(self, username: str = None, password: str = None) -> str:
        raise NotImplementedError("Authenticate method not implemented")

    def _get_host(self) -> str:
        url = urlparse(self._server)
        return f"{url.scheme}://{url.netloc}"
