import allure
import requests

from Core.models.booking import BookingResponse
from pydantic import ValidationError
import pytest
from Core.models.checking import CheckStatusCode


@allure.feature('Тесты на создание бронирования отеля')
class TestsCreateBookings:
    @allure.story('Создание бронирования')
    def test_create(self, api_client):
        booking_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "lunch"
        }
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
            assert response_json["booking"]["firstname"] == booking_data[
                "firstname"], 'firstname запроса не совпадает с firstname ответа'
            assert response_json["booking"]["lastname"] == booking_data[
                "lastname"], 'lastname запроса не совпадает с lastname ответа'
            assert response_json["booking"]["totalprice"] == booking_data[
                "totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
            assert response_json["booking"]["depositpaid"] == booking_data[
                "depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
            assert response_json["booking"]["additionalneeds"] == booking_data[
                "additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
            assert response_json["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"][
                "checkin"], 'checkin запроса не совпадает с checkin ответа'
            assert response_json["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"][
                "checkout"], 'checkout запроса не совпадает с checkout ответа'

    @allure.story('Создание бронирования с рандомным телом')
    def test_create_random(self, api_client, generate_random_booking_data, booking_dates):
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
            assert response_json["booking"]["firstname"] == booking_data[
                "firstname"], 'firstname запроса не совпадает с firstname ответа'
            assert response_json["booking"]["lastname"] == booking_data[
                "lastname"], 'lastname запроса не совпадает с lastname ответа'
            assert response_json["booking"]["totalprice"] == booking_data[
                "totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
            assert response_json["booking"]["depositpaid"] == booking_data[
                "depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
            assert response_json["booking"]["additionalneeds"] == booking_data[
                "additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
            assert response_json["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"][
                "checkin"], 'checkin запроса не совпадает с checkin ответа'
            assert response_json["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"][
                "checkout"], 'checkout запроса не совпадает с checkout ответа'

    @allure.story('Создание бронирования с пустыми значением "totalprice"')
    def test_create_booking_invalid_data(self, api_client):
        booking_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": None,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "lunch"
        }
        with allure.step('Отправка запроса на подключение'):
            try:
                response = api_client.create_booking(booking_data)
                pytest.fail("Ожидалась 500 ошибка, но запрос завершился успешно")
            except requests.exceptions.HTTPError as e:
                response = e.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_500(response)

    @allure.story('Создание бронирования с невалидным значением "firstname"')
    def test_create_booking_invalid_data(self, api_client):
        booking_data = {
            "firstname": 111,
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "lunch"
        }
        with allure.step('Отправка запроса на подключение'):
            try:
                response = api_client.create_booking(booking_data)
                pytest.fail("Ожидалась 500 ошибка, но запрос завершился успешно")
            except requests.exceptions.HTTPError as e:
                response = e.response
        with allure.step('Проверка статус кода'):
            CheckStatusCode.check_500(response)
