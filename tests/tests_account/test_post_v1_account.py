from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel


def test_post_v1_account(account_api):
    response = account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login='test_user_5',
            email='test_user_5@mail.ru',
            password='test_user_5'
        )
    )
    assert response.status_code == 201
