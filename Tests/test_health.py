import allure
from Core.models.checking import CheckStatusCode


@allure.feature('Тест подключения')
class TestsPing:
    @allure.title('Проверка подключения')
    def test_ping(self, api_client):
        status_code = api_client.ping()
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_201(status_code)