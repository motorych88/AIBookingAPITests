import pytest
import allure
import requests


@allure.feature('Тесты на создание бронирования отеля')
class TestsCreateBookings:
    @allure.story('Создание бронирования')
    def test_create(self, api_client, generate_random_booking_data, booking_dates):
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        with allure.step('Отправка запроса на подключение'):
            response_data = api_client.create_booking(booking_data)
        with allure.step('Проверка полей ответа'):
            assert response_data["booking"]["firstname"] == booking_data["firstname"], 'firstname запроса не совпадает с firstname ответа'
            assert response_data["booking"]["lastname"] == booking_data["lastname"], 'lastname запроса не совпадает с lastname ответа'
            assert response_data["booking"]["totalprice"] == booking_data["totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
            assert response_data["booking"]["depositpaid"] == booking_data["depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
            assert response_data["booking"]["additionalneeds"] == booking_data["additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
            assert response_data["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], 'checkin запроса не совпадает с checkin ответа'
            assert response_data["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], 'checkout запроса не совпадает с checkout ответа'








