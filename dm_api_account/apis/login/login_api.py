from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from restclient.restclient import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self.headers

    def post_v1_account_login(self, json_data: LoginCredentialsRequestModel):
        headers = {
            'accept': 'text/plain',
        }

        response = self.client.post(
            path=f'/v1/account/login',
            headers=headers,
            json=json_data.to_struct()
        )
        return response
