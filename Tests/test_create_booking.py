import allure
import requests
from Core.models.check_json import CheckResponseJson
from Core.models.booking import BookingResponse
from pydantic import ValidationError
import pytest
from Core.models.checking import CheckStatusCode


@allure.feature('Тесты на создание бронирования отеля')
class TestsCreateBookings:
    @allure.title('Создание бронирования')
    def test_create(self, api_client, create_booking_static_payload):
        booking_data = create_booking_static_payload
        with allure.step('Отправка запроса на подключение'):
            response = api_client.create_booking(booking_data)
            response_json = response.json()
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response)
            try:
                BookingResponse(**response_json)
            except ValidationError as e:
                raise ValidationError(f'Ответ не прошел валидацию {e}')
        with allure.step('Проверка полей ответа'):
            CheckResponseJson.check_booking_response_json(response_json, booking_data)

    @allure.title('Создание бронирования с рандомным телом')
    def test_create_random(self, api_client, generate_random_booking_data, booking_dates, create_booking_static_payload):
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        with allure.step('Отправка запроса на подключение'):
            response = api_client.create_booking(booking_data)
            response_json = response.json()
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response)
            try:
                BookingResponse(**response_json)
            except ValidationError as e:
                raise ValidationError(f'Ответ не прошел валидацию {e}')
        with allure.step('Проверка полей ответа'):
            CheckResponseJson.check_booking_response_json(response_json, booking_data)

    @allure.title('Создание бронирования с пустыми значением "totalprice"')
    def test_create_booking_empty_data(self, api_client, create_booking_static_payload):
        booking_data = create_booking_static_payload
        booking_data["totalprice"] = None
        with allure.step('Отправка запроса на подключение'):
            with pytest.raises(requests.exceptions.HTTPError) as e:
                api_client.create_booking(booking_data)
            response = e.value.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_500(response)

    @allure.title('Создание бронирования с невалидным значением "firstname"')
    def test_create_booking_invalid_data(self, api_client, create_booking_static_payload):
        booking_data = create_booking_static_payload
        booking_data["firstname"] = 111
        with allure.step('Отправка запроса на подключение'):
            with pytest.raises(requests.exceptions.HTTPError) as e:
                api_client.create_booking(booking_data)
            response = e.value.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_500(response)
