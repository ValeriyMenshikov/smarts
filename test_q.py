import pprint
import json
import requests


def test_post_v1_account():
    headers = {
        'accept': '*/*',
    }

    json_data = {
        'login': 'test_user_1',
        'email': 'test_user_1@mail.ru',
        'password': 'test_user_1',
    }

    response = requests.post('http://localhost:5051/v1/account', headers=headers, json=json_data)


def test_put_v1_account_token():
    headers = {
        'accept': 'text/plain',
    }
    response = requests.put('http://localhost:5051/v1/account/a894dc9c-a044-45d0-9109-4d34cefa5594', headers=headers)


def test_post_v1_account_login():
    headers = {
        'accept': 'text/plain',
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }

    json_data = {
        'login': 'test_user_1',
        'password': 'test_user_1',
        'rememberMe': True,
    }

    response = requests.post('http://localhost:5051/v1/account/login', headers=headers, json=json_data)


def test_get_v1_account():
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': 'IQJh+zgzF5CaWwvi75Y1RgP+v1S+kL2/NLwGqk2R4o8DjpNSFfaqHrKnZJzjoeSMbo9NQS1srkI9HiUsZOpErIFyfPyQBztlvEDxdtxIbeW+eZ39cbRq20IymjSaM1Kx0d3tG+ocX3s=',
    }

    response = requests.get('http://localhost:5051/v1/account', headers=headers)
    print()
    # pprint.pprint(response.text)
    # print(response.headers)
    # print(response.status_code)
    # pprint.pprint(response.json())
    # print(response.url)
    # print(response.content)


def test_get_all_email():
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
    print()
    pprint.pprint(token)
    return token

