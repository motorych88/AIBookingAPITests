import allure
import requests
from Core.models.booking import Booking
from pydantic import ValidationError
import pytest
from Core.models.check_json import CheckResponseJson
from Core.models.checking import CheckStatusCode


@allure.feature('Тесты на Обновление бронирования отеля')
class TestsUpdateBookings:
    @allure.title('Обновление бронирования')
    def test_update(self, api_client, generate_random_booking_data, booking_dates, create_booking_static_payload):
        booking_data_create = create_booking_static_payload
        with allure.step('Отправка запроса на создание бронирования'):
            response_create = api_client.create_booking(booking_data_create)
            response_json_create =  response_create.json()
            booking_id = response_json_create["bookingid"]
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response_create)
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        with allure.step('Отправка запроса на обновление бронирования'):
            response_update = api_client.update_booking(booking_data, booking_id)
            response_json = response_update.json()
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response_update)
            try:
                Booking(**response_json)
            except ValidationError as e:
                raise ValidationError(f'Ответ не прошел валидацию {e}')
        with allure.step('Проверка полей ответа'):
            CheckResponseJson.check_update_booking_response_json(response_json, booking_data)

    @allure.title('Попытка обновления бронирования без параметра ID')
    def test_update_no_id(self, api_client, generate_random_booking_data, booking_dates, create_booking_static_payload):
        booking_data_create = create_booking_static_payload
        with allure.step('Отправка запроса на создание бронирования'):
            response_create = api_client.create_booking(booking_data_create)
            booking_id = None
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response_create)
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        with allure.step('Отправка запроса на обновление бронирования'):
            with pytest.raises(requests.exceptions.HTTPError) as e:
                api_client.update_booking(booking_data, booking_id)
            response = e.value.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_405(response)

    @allure.title('Попытка обновления бронирования без с пустым значением в теле')
    def test_update_empty(self, api_client, generate_random_booking_data, booking_dates, create_booking_static_payload):
        booking_data_create = create_booking_static_payload
        with allure.step('Отправка запроса на создание бронирования'):
            response_create = api_client.create_booking(booking_data_create)
            response_json_create = response_create.json()
            booking_id = response_json_create["bookingid"]
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response_create)
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        booking_data["totalprice"] = None
        with allure.step('Отправка запроса на обновление бронирования'):
            with pytest.raises(requests.exceptions.HTTPError) as e:
                api_client.update_booking(booking_data, booking_id)
            response = e.value.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_400(response)

    @allure.title('Попытка обновления бронирования без с невалидным значением в теле')
    def test_update_invalid(self, api_client, generate_random_booking_data, booking_dates, create_booking_static_payload):
        booking_data_create = create_booking_static_payload
        with allure.step('Отправка запроса на создание бронирования'):
            response_create = api_client.create_booking(booking_data_create)
            response_json_create = response_create.json()
            booking_id = response_json_create["bookingid"]
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_200(response_create)
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        booking_data["firstname"] = 111
        with allure.step('Отправка запроса на обновление бронирования'):
            with pytest.raises(requests.exceptions.HTTPError) as e:
                api_client.update_booking(booking_data, booking_id)
            response = e.value.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_500(response)