from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel


def test_get_v1_account(dm_api_account):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_4',
            password='test_user_4',
        )
    )
    token = response.headers['X-Dm-Auth-Token']
    response = dm_api_account.account_api.get_v1_account(
        x_dm_auth_token=token
    )
    assert response.resource.login == 'test_user_4'
