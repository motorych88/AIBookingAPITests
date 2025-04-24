import allure
import requests
from requests.auth import HTTPBasicAuth
from Core.Clients import endpoints
from Core.Clients.endpoints import Endpoints
from Core.Settings.config import Users, Timeouts


class APIClient:
    def __init__(self):
        self.base_url = endpoints.BASE_URL
        self.session = requests.session()
        self.session.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get(self, endpoint, params=None, expected_status_code=200):
        url = f'{self.base_url}/{endpoint}'
        response = self.session.get(url, params=params)
        if expected_status_code:
            assert response.status_code == expected_status_code
        return response.json()

    def post(self, endpoint, data=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.session.headers, json=data)
        if status_code:
            assert response.status_code == status_code
        return response

    def ping(self):
        with allure.step('Ping Api client'):
            url = f'{self.base_url}/{Endpoints.PING_ENDPOINT.value}'
            response = self.session.get(url)
            response.raise_for_status()
        return response

    def auth(self):
        with allure.step('Запрос на авторизацию'):
            url = f'{self.base_url}/{Endpoints.AUTH_ENDPOINT.value}'
            payload = {"username": Users.USERNAME.value, "password": Users.PASSWORD.value}
            response = self.session.post(url, json=payload, timeout=Timeouts.TIMEOUT.value)
        token = response.json().get('token')
        with allure.step('Добавление Token в заголовки'):
            self.session.headers.update({"Authorization": f'Bearer {token}'})

    def get_booking_by_id(self, booking_id='1'):
        with allure.step('Поиск отеля по ID'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}'
            response = self.session.get(url, headers=self.session.headers)
            response.raise_for_status()
        return response

    def delete_booking(self, booking_id='1'):
        with allure.step('Удаление отеля по ID'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT}/{booking_id}'
            response = self.session.delete(url, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value))
            response.raise_for_status()
        return response

    def create_booking(self, booking_data):
        with allure.step('Создание отеля'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT.value}'
            response = self.session.post(url, json=booking_data)
            response.raise_for_status()
        return response

    def get_bookings(self, params=None):
        with allure.step('Search bookings'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT.value}'
            response = self.session.post(url, params)
        return response

    def update_booking(self, update_body, booking_id='1'):
        with allure.step('Update booking'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}'
            response = self.session.put(url, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value),json=update_body)
            response.raise_for_status()
        return response

    def partial_update_booking(self, partial_update_body, booking_id='1'):
        with allure.step('Частичное редактирование отеля'):
            url = f'{self.base_url}/{Endpoints.BOOKING_ENDPOINT.value}/{booking_id}'
            response = self.session.patch(url, auth=HTTPBasicAuth(Users.USERNAME.value, Users.PASSWORD.value),json=partial_update_body)
            response.raise_for_status()
        return response
