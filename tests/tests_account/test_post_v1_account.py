import pytest
from hamcrest import assert_that, has_entries
from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel


def test_post_v1_account(dm_api_account, dm_db):
    login = 'test_user_5'
    dm_db.delete_user_by_login(login)
    response = dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login='test_user_5',
            email='test_user_5@mail.ru',
            password='test_user_5'
        )
    )
    assert response.status_code == 201


@pytest.mark.parametrize('login, email, password', [('test_user_5', 'test_user_5@mail.ru', 'test_user_5')])
def test_registration_user(login, email, password, dm_api_account, dm_db, mailhog, assertions):
    dm_db.delete_user_by_login(login)
    mailhog.delete_all_emails()
    dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login=login,
            email=email,
            password=password
        )
    )
    user_email = mailhog.get_email_by_user_name(user_name=login)
    assert user_email
    token = mailhog.get_token_from_email(user_email[0])
    dm_api_account.account_api.put_v1_account_token(token=token)
    assertions.assert_all(email, login)


@pytest.mark.parametrize('login, email, password', [('test_user_6', 'test_user_6@mail.ru', 'test_user_6')])
def test_registration_user2(login, email, password, dm_api_account, dm_db, mailhog, assertions):
    dm_db.delete_user_by_login(login)
    mailhog.delete_all_emails()
    dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login=login,
            email=email,
            password=password
        )
    )
    user_email = mailhog.get_email_by_user_name(user_name=login)
    assert user_email
    token = mailhog.get_token_from_email(user_email[0])
    dm_api_account.account_api.put_v1_account_token(token=token)
    assertions.assert_db_state(email, login)
