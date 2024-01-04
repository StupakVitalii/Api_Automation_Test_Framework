import json
import os

import requests
import allure


class ApiService(object):
    def __init__(self):
        self._base_url = os.environ['BASE_URL']

    @allure.step('GET: {endpoint}')
    def _get(self, endpoint, headers):
        return requests.get(f"{self._base_url}{endpoint}", headers=headers)

    @allure.step('POST: {endpoint}')
    def _post(self, endpoint, body, headers):
        return requests.post(f"{self._base_url}{endpoint}", data=json.dumps(body), headers=headers)

    @allure.step('PUT: {endpoint}')
    def _put(self, endpoint, body, headers):
        return requests.put(f"{self._base_url}{endpoint}", data=body, headers=headers)

    @allure.step('DELETE: {endpoint}')
    def _delete(self, endpoint, headers):
        return requests.delete(f"{self._base_url}{endpoint}", headers=headers)


class UserApiService(ApiService):
    def __init__(self):
        super().__init__()

    @allure.step
    def get_user_current(self, headers):
        return self._get(endpoint="/users/current", headers=headers)

    @allure.step
    def get_user_profile(self, headers):
        return self._get(endpoint="/users/profile", headers=headers)

    def get_user_settings(self, headers):
        return self._get(endpoint="/users/settings", headers=headers)

    @allure.step
    def edit_user_profile(self, body, headers):
        return self._put(endpoint="/users/profile", body=body, headers=headers)

    @allure.step
    def edit_user_settings(self, body, headers):
        return self._put(endpoint="/users/settings", body=body, headers=headers)

    @allure.step
    def change_user_email(self, body, headers):
        return self._put(endpoint="/users/email", body=body, headers=headers)

    @allure.step
    def change_user_password(self, body, headers):
        return self._put(endpoint="/users/password", body=body, headers=headers)

    @allure.step
    def delete_user(self, headers):
        return self._delete(endpoint="/users", headers=headers)


class CarApiService(ApiService):
    def __init__(self):
        super().__init__()
