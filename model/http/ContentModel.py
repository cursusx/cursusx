from abc import ABC
from dataclasses import dataclass
from http import HTTPStatus

from model.http.BodyModel import AbstractBody
from model.http.HeaderModel import Headers


class AbstractContentMethod(ABC):
    """
    This class represents a http http, it has a collection of headers and a
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
        This http returns the current http status code.
        :return: see above
        """
        return self._my_status_code

    def get_headers(self) -> Headers:
        """
        This http returns the collection of headers.
        :return: see above
        """
        return self._my_headers

    def get_body(self) -> AbstractBody:
        """
        This http returns the body of the http http.
        :return: see above
        """
        return self._my_body

class ResponseContent(AbstractContentMethod):
    """
    This class represents a Response http http.
    """
    def __init__(self, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(status_code, headers, body)

class RequestContent(AbstractContentMethod):
    """
    This class represents a Request http http.
    """
    def __init__(self, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(status_code, headers, body)
