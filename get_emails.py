import pprint

import requests
import json


def get_all_email():
    cookies = {
        'MANTIS_secure_session': '0',
        'PHPSESSID': 'm2uc795c7p4aasmvm81814bc78',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-XA;q=0.8,en;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'MANTIS_secure_session=0; PHPSESSID=m2uc795c7p4aasmvm81814bc78',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'limit': '50',
    }

    response = requests.get('http://localhost:5025/api/v2/messages', params=params, cookies=cookies, headers=headers)
    # pprint.pprint(response.json())
    emails = response.json()
    items = emails['items']
    content_user = items[0]
    content = content_user['Content']
    body = content['Body']
    json_ = json.loads(body)
    confirmation_link_url = json_['ConfirmationLinkUrl']
    token = confirmation_link_url.split('/')[-1]
    return token


print(get_all_email())