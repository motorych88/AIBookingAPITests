import allure
from Core.models.booking import BookingResponse
from pydantic import ValidationError


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
            try:
                BookingResponse(**response)
            except ValidationError as e:
                raise ValidationError(f'Ответ не прошел валидацию {e}')
        with allure.step('Проверка полей ответа'):
            assert response["booking"]["firstname"] == booking_data[
                "firstname"], 'firstname запроса не совпадает с firstname ответа'
            assert response["booking"]["lastname"] == booking_data[
                "lastname"], 'lastname запроса не совпадает с lastname ответа'
            assert response["booking"]["totalprice"] == booking_data[
                "totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
            assert response["booking"]["depositpaid"] == booking_data[
                "depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
            assert response["booking"]["additionalneeds"] == booking_data[
                "additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
            assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"][
                "checkin"], 'checkin запроса не совпадает с checkin ответа'
            assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"][
                "checkout"], 'checkout запроса не совпадает с checkout ответа'

    @allure.story('Создание бронирования с рандомным телом')
    def test_create_random(self, api_client, generate_random_booking_data, booking_dates):
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
        with allure.step('Отправка запроса на подключение'):
            response = api_client.create_booking(booking_data)
            try:
                BookingResponse(**response)
            except ValidationError as e:
                raise ValidationError(f'Ответ не прошел валидацию {e}')
        with allure.step('Проверка полей ответа'):
            assert response["booking"]["firstname"] == booking_data[
                "firstname"], 'firstname запроса не совпадает с firstname ответа'
            assert response["booking"]["lastname"] == booking_data[
                "lastname"], 'lastname запроса не совпадает с lastname ответа'
            assert response["booking"]["totalprice"] == booking_data[
                "totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
            assert response["booking"]["depositpaid"] == booking_data[
                "depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
            assert response["booking"]["additionalneeds"] == booking_data[
                "additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
            assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"][
                "checkin"], 'checkin запроса не совпадает с checkin ответа'
            assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"][
                "checkout"], 'checkout запроса не совпадает с checkout ответа'
