import allure


class CheckResponseJson:
    @staticmethod
    @allure.step('Проверка полей ответа создания бронирования')
    def check_booking_response_json(response_json, booking_data):
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

    @staticmethod
    @allure.step('Проверка полей ответа редактирования бронирования')
    def check_update_booking_response_json(response_json, booking_data):
        assert response_json["firstname"] == booking_data["firstname"], 'firstname запроса не совпадает с firstname ответа'
        assert response_json["lastname"] == booking_data["lastname"], 'lastname запроса не совпадает с lastname ответа'
        assert response_json["totalprice"] == booking_data["totalprice"], 'totalprice запроса не совпадает с totalprice ответа'
        assert response_json["depositpaid"] == booking_data["depositpaid"], 'depositpaid запроса не совпадает с depositpaid ответа'
        assert response_json["additionalneeds"] == booking_data["additionalneeds"], 'additionalneeds запроса не совпадает с additionalneeds ответа'
        assert response_json["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], 'checkin запроса не совпадает с checkin ответа'
        assert response_json["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], 'checkout запроса не совпадает с checkout ответа'
