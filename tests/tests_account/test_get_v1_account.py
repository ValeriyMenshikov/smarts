import allure

from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from hamcrest import assert_that, empty, has_entries, has_properties
from datetime import datetime
import jsondiff


@allure.description("test")
def test_get_v1_account(dm_api_account):
    with allure.step('Get account info'):
        response = dm_api_account.account_api.get_v1_account()
    assert_that(response.resource, has_properties(
        {
            "login": "test_user_4",
            # "registration": "2022-08-26T07:13:05.539326+00:00",
            "roles": [
                "Guest",
                "Player"
            ],
        }
    ))
    # assert_that(jsondiff.diff(response, expected), empty())
