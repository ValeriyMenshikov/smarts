import requests


class LoginApi:
    def __init__(self, host):
        self.host = host

    def post_v1_account_login(self, login, password, remember_me):
        headers = {
            'accept': 'text/plain',
        }

        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me,
        }

        response = requests.post(
            url=f'{self.host}/v1/account/login',
            headers=headers,
            json=json_data
        )
        return response
