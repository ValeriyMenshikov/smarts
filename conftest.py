import pytest
import structlog
from dm_api_account.apis import AccountApi, LoginApi
from helpers.mailhog.mailhog_client import MailHogClient

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


@pytest.fixture
def account_api():
    return AccountApi(host='http://localhost:5051')


@pytest.fixture
def login_api():
    return LoginApi(host='http://localhost:5051')


@pytest.fixture
def mailhog():
    return MailHogClient(host='http://localhost:5025')
