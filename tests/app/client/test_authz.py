from unittest.mock import patch

from genetic_forensic_portal.app.client import keycloak_client
from genetic_forensic_portal.app.client.models.analysis_permissions import (
    Action,
)

TEST_USER = "test_user"
TEST_RESOURCE = "test_resource"


# user: T resource: T decision: True
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: True, Action.DOWNLOAD: True}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: True, Action.DOWNLOAD: True}}},
)
def test_user_allowed_resource_allowed_access_allowed():
    assert keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)


# user: N resource: T decision: True
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: None, Action.DOWNLOAD: None}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: True, Action.DOWNLOAD: True}}},
)
def test_user_not_defined_resource_allowed_access_allowed():
    assert keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)


# user: F resource: T decision: False
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: False, Action.DOWNLOAD: False}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: True, Action.DOWNLOAD: True}}},
)
def test_user_denied_resource_allowed_access_denied():
    assert not keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert not keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)


# user: T resource: F decision: False
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: True, Action.DOWNLOAD: True}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: False, Action.DOWNLOAD: False}}},
)
def test_user_allowed_resource_denied_access_denied():
    assert not keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert not keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)


# user: N resource: F decision: False
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: None, Action.DOWNLOAD: None}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: False, Action.DOWNLOAD: False}}},
)
def test_user_not_defined_resource_denied_access_denied():
    assert not keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert not keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)


# user: F resource: F decision: False
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_USER_AUTH_CACHE",
    {TEST_USER: {Action.VIEW: False, Action.DOWNLOAD: False}},
)
@patch(
    "genetic_forensic_portal.app.client.keycloak_client.MOCK_RESOURCE_AUTH_CACHE",
    {TEST_RESOURCE: {TEST_USER: {Action.VIEW: False, Action.DOWNLOAD: False}}},
)
def test_user_denied_resource_denied_access_denied():
    assert not keycloak_client.check_view_access(TEST_USER, [], TEST_RESOURCE)
    assert not keycloak_client.check_download_access(TEST_USER, [], TEST_RESOURCE)
