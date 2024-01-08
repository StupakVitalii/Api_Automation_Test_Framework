import random
import json
import requests
from src.services import CarApiService
car_api = CarApiService()


def test_create_new_car(sign_up_response):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    headers_1 = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.create_new_car(body=payload, headers=headers_1)
    response_json = response.json()
    car_id = response_json['data']['id']
    assert response.status_code == 201
    assert response_json['status'] == 'ok'
    assert response_json['data']['carBrandId'] == int(payload.split()[1][0])


def test_get_car_brand(sign_up_response):
    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.get_car_brand(headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'


def test_get_car_brand_by_id(sign_up_response):
    random_id = random.randint(1, 5)
    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.get_car_brand_by_id(headers=headers, random=random_id)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'
    assert response_json['data']['id'] == random_id


def test_get_cars_model(sign_up_response):
    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.get_cars_model(headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'


def test_get_car_model_by_id(sign_up_response):
    random_id = random.randint(1, 23)
    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.get_car_model_by_id(headers=headers, random=random_id)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'
    assert response_json['data']['id'] == random_id


def test_get_current_user_car_by_id(sign_up_response):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    headers_1 = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response_tempo = car_api.create_new_car(body=payload, headers=headers_1)
    response_json = response_tempo.json()
    car_id = response_json['data']['id']
    payload = {}
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.get_current_user_car_by_id(headers=headers, created_car_id=car_id)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'


def test_edit_existing_car(sign_up_response):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    headers_1 = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response_tempo = car_api.create_new_car(body=payload, headers=headers_1)
    response_json = response_tempo.json()
    car_id = response_json['data']['id']
    payload = json.dumps({
        "carBrandId": 2,
        "carModelId": 6,
        "mileage": 168223
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.edit_existing_car(body=payload, headers=headers, created_car_id = car_id)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'
    assert response_json['data']['mileage'] == int(payload.split()[5][:-1])
    assert response_json['data']['carBrandId'] == int(payload.split()[1][:-1])


def test_delete_existing_car(sign_up_response):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    headers_1 = {
        'Content-Type': 'application/json',
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response_tempo = car_api.create_new_car(body=payload, headers=headers_1)
    response_json = response_tempo.json()
    car_id = response_json['data']['id']
    headers = {
        'Cookie': f'sid={sign_up_response.cookies.get("sid")}'
    }
    response = car_api.delete_existing_car(headers=headers, created_car_id=car_id)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'ok'
    print(response.text)
