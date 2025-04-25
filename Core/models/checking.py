
class CheckStatusCode:

    @staticmethod
    def check_200(response):
        assert response.status_code == 200, f'Ожидаемый статус код 200, получили: {response.status_code}'
        return response

    @staticmethod
    def check_201(response):
        assert response.status_code == 201, f'Ожидаемый статус код 201, получили: {response.status_code}'
        return response

    @staticmethod
    def check_400(response):
        assert response.status_code == 400, f'Ожидаемый статус код 400, получили: {response.status_code}'
        return response

    @staticmethod
    def check_405(response):
        assert response.status_code == 405, f'Ожидаемый статус код 405, получили: {response.status_code}'
        return response


    @staticmethod
    def check_500(response):
        assert response.status_code == 500, f'Ожидаемый статус код 500, получили: {response.status_code}'
        return response
