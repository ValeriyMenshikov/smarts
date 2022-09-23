import requests
from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel
from dm_api_account.models.account.get_v1_account_response_model import UserDetailsEnvelopeResponseModel
from restclient.restclient import RestClient






class AccountApi:
    def __init__(self, host='http://localhost:5051', headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self.headers

    def post_v1_account(self, json_data: RegistrationRequestModel):
        headers = {
            'accept': '*/*',
        }

        response = self.client.post(
            path=f'/v1/account',
            headers=headers,
            json=json_data.to_struct()
        )
        return response

    def put_v1_account_token(self, token):
        headers = {
            'accept': 'text/plain',
        }
        response = self.client.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        return response

    def get_v1_account(self, x_dm_auth_token) -> UserDetailsEnvelopeResponseModel:
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = self.client.get(
            path=f'/v1/account',
            headers=headers
        )
        response_json = response.json()
        return UserDetailsEnvelopeResponseModel(**response_json)
