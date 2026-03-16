from abc import ABC
from http import HTTPStatus

from model.method.HeaderModel import Headers


class AbstractMethod(ABC):
    """
    This class represents a http method, it has a collection of headers and a
    status code
    """
    _my_status_code: HTTPStatus
    _my_headers: Headers

    def __init__(self, status_code: HTTPStatus, headers: Headers) -> None:
        self._my_status_code = status_code
        self._my_headers = headers

    def get_status_code(self) -> HTTPStatus:
        return self._my_status_code

    def get_headers(self) -> Headers:
        return self._my_headers
