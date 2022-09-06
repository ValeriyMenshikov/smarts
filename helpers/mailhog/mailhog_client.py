import json
import pprint
import re

import requests


class MailHogClient:
    def __init__(self, host='http://localhost:5025'):
        self.host = host

    def get_all_email(self, limit=50):
        params = {
            'limit': str(limit),
        }

        response = requests.get(
            url=f'{self.host}/api/v2/messages',
            params=params
        )
        return response

    def get_token_from_last_email(self):
        emails = self.get_all_email(limit=1)
        token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def get_token(self, user, token_type):
        response = self.get_all_email()
        token = None
        for email in response.json()['items']:
            content = json.loads(email['Content']['Body'])
            if re.findall(f'ConfirmationLinkUrl.*{token_type}', str(content)):
                if content['Login'] == user:
                    token = content['ConfirmationLinkUrl'].split('/')[-1]
        return token
