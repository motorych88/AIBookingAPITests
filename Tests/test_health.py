import pytest
import allure
import requests


@allure.feature('Тест Ping')
class TestsPing:
    @allure.story('Проверка подключения')
    def test_ping(self, api_client):
        status_code = api_client.ping()
        with allure.step('Проверка статус кода'):
            assert status_code == 201, f'Ожидаемый статус код 201, получили: {status_code}'
