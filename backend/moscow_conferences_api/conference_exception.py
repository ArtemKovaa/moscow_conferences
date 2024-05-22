from rest_framework import exceptions


class ConferenceException(exceptions.APIException):
    def __init__(self, detail: str = 'Error processing request', status_code: int = 400):
        self.detail = detail
        self.status_code = status_code
