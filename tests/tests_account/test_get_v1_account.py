from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel


def test_get_v1_account(account_api, login_api):
    response = login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_4',
            password='test_user_4',
        )
    )
    token = response.headers['X-Dm-Auth-Token']
    response = account_api.get_v1_account(
        x_dm_auth_token=token
    )
