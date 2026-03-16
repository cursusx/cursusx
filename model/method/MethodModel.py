from abc import ABC
from dataclasses import dataclass
from http import HTTPStatus

from model.method.BodyModel import AbstractBody
from model.method.HeaderModel import Headers


class AbstractMethod(ABC):
    """
    This class represents a http method, it has a collection of headers and a
    status code
    """
    _my_status_code: HTTPStatus
    _my_headers: Headers
    _my_body: AbstractBody

    def __init__(self, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        self._my_status_code = status_code
        self._my_headers = headers
        self._my_body = body

    def get_status_code(self) -> HTTPStatus:
        """
        This method returns the current http status code.
        :return: see above
        """
        return self._my_status_code

    def get_headers(self) -> Headers:
        """
        This method returns the collection of headers.
        :return: see above
        """
        return self._my_headers

    def get_body(self) -> AbstractBody:
        """
        This method returns the body of the http method.
        :return: see above
        """
        return self._my_body

class ResponseMethod(AbstractMethod):
    """
    This class represents a Response http method.
    """
    def __init__(self, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(status_code, headers, body)

class RequestMethod(AbstractMethod):
    """
    This class represents a Request http method.
    """
    def __init__(self, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(status_code, headers, body)