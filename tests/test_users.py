import random
import requests
import json

URL = "https://qauto.forstudy.space/api"


def test_get_authenticated_user_data(sign_up_response):
    url = f"{URL}/users/current"

    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=5)

    assert response.status_code == 200, 'Status code broken'
    response_json = response.json()
    assert response_json['status'] == 'ok'
    assert response_json['data']['userId'] == sign_up_response.json()['data']['userId']


def test_get_authenticated_user_profile_data(sign_up_response):
    url = f"{URL}/users/profile"

    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    sign_up_response_request_body = json.loads(sign_up_response.request.body)

    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['userId'] == sign_up_response.json()['data']['userId']
    assert response_json['data']['name'] == sign_up_response_request_body['name']
    assert response_json['data']['lastName'] == sign_up_response_request_body['lastName']
    print()


def test_get_authenticated_user_settings_data(sign_up_response):
    url = f"{URL}/users/settings"

    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
    print(response)
    response_json = response.json()
    sign_up_response_request_body = json.loads(sign_up_response.request.body)

    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['currency'] == sign_up_response.json()['data']['currency']
    assert response_json['data']['distanceUnits'] == sign_up_response.json()['data']['distanceUnits']
    print()


def test_edit_user_profile(sign_up_response):
    url = f"{URL}/users/profile"

    payload = json.dumps({
        "photo": "user-1621352948859.jpg",
        "name": "John",
        "lastName": "Dou",
        "dateBirth": "2021-03-17T15:21:05.000Z",
        "country": "Ukraine"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }

    response = requests.request('PUT', url, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    payload_json = json.loads(payload)
    sign_up_response_request_body = json.loads(sign_up_response.request.body)
    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['userId'] == sign_up_response.json()['data']['userId']
    assert response_json['data']['photoFilename'] == sign_up_response.json()['data']['photoFilename']
    assert response_json['data']['name'] == sign_up_response_request_body['name']
    assert response_json['data']['lastName'] == sign_up_response_request_body['lastName']
    assert response_json['data']['dateBirth'] == payload_json['dateBirth']
    assert response_json['data']['country'] == payload_json['country']
    print()


def test_edits_users_settings(sign_up_response):
    url = f"{URL}/users/settings"

    payload = json.dumps({
        "currency": "usd",
        "distanceUnits": "km"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }

    response = requests.request('PUT', url, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    payload_json = json.loads(payload)
    sign_up_response_request_body = json.loads(sign_up_response.request.body)
    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['currency'] == payload_json['currency']
    assert response_json['data']['distanceUnits'] == payload_json['distanceUnits']
    print()


def test_changes_users_email(sign_up_response):
    url = f"{URL}/users/email"

    sign_up_response_request_body = json.loads(sign_up_response.request.body)
    password_value = sign_up_response_request_body['password']

    payload = json.dumps({
        "email": f"qweerty{random.randint(100000, 999999)}@mail.com",
        "password": f"{password_value}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = requests.request('PUT', url, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['userId'] == sign_up_response.json()['data']['userId']

    print()

def test_changes_users_password(sign_up_response):
    url = f"{URL}/users/password"

    sign_up_response_request_body = json.loads(sign_up_response.request.body)
    password_value = sign_up_response_request_body['password']
    new_password_value = 'new'+password_value

    payload = json.dumps({
        "oldPassword": f"{password_value}",
        "password": f"{new_password_value}",
        "repeatPassword": f"{new_password_value}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = requests.request('PUT', url, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'
    assert response_json['data']['userId'] == sign_up_response.json()['data']['userId']

    print()


def test_delete_users_account_and_session(sign_up_response):
    url = f"{URL}/users"

    payload = {
    }

    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = requests.request('DELETE', url, headers=headers, data=payload, timeout=5)
    response_json = response.json()

    assert response.status_code == 200, 'Status code broken'
    assert response_json['status'] == 'ok'

    print()