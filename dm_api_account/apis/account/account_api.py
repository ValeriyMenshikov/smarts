import requests
from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel
from dm_api_account.models.account.get_v1_account_response_model import UserDetailsEnvelopeResponseModel
from restclient.restclient import RestClient


class AccountApi:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self.headers

    def post_v1_account(self, json_data: RegistrationRequestModel):
        response = self.client.post(
            path=f'/v1/account',
            json=json_data.to_struct()
        )
        return response

    def put_v1_account_token(self, token):
        response = self.client.put(path=f'/v1/account/{token}')
        return response

    def get_v1_account(self, status_code=200) -> UserDetailsEnvelopeResponseModel:
        response = self.client.get(path=f'/v1/account')
        response_json = response.json()
        assert response.status_code == status_code
        return UserDetailsEnvelopeResponseModel(**response_json)
