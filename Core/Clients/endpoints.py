from enum import Enum

BASE_URL = 'https://restful-booker.herokuapp.com'

class Endpoints(Enum):
    PING_ENDPOINT = 'ping'
    AUTH_ENDPOINT = 'auth'
    BOOKING_ENDPOINT = 'booking'