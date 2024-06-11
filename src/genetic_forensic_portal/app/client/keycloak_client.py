from __future__ import annotations

from typing import Any

from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="gf-portal-login",
    realm_name="gf-portal",
)


def login_user(username: str, password: str) -> Any:
    return keycloak_openid.token(username, password)


def logout_user(token: dict[Any, Any]) -> None:
    keycloak_openid.logout(token["refresh_token"])
