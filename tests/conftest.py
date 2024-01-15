import os
import pytest
import requests
import json
import random

from tests.test_cars import car_api


@pytest.fixture(scope='session')
def sign_up_response(url):
    payload = json.dumps({
        "name": "John",
        "lastName": "Dou",
        "email": f"qweerty{random.randint(100000, 999999)}@mail.com",
        "password": "Test12341",
        "repeatPassword": "Test12341"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", f"{url}/auth/signup", headers=headers, data=payload, timeout=5)
    return response


@pytest.fixture(scope='session')
def headers(sign_up_response):
    return {'Cookie': f'sid={sign_up_response.cookies.get("sid")}'}


@pytest.fixture(scope='session')
def url():
    return os.environ['BASE_URL']


@pytest.fixture(scope='session')
def car_id(sign_up_response, headers):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    response = car_api.create_new_car(body=payload, headers=headers)
    return response.get_field('data')['id']
