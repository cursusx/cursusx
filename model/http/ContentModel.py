from abc import ABC
from http import HTTPStatus

from model.endpoint.EndPointModel import AbstractEndpoint
from model.http.BodyModel import AbstractBody
from model.http.HeaderModel import Headers

#TODO: ADD TESTS

class AbstractContent(ABC):
    """
    This class represents a http method.
    It has an endpoint, a status code, a collection of headers and a body.
    """
    _my_endpoint: AbstractEndpoint
    _my_status_code: HTTPStatus
    _my_headers: Headers
    _my_body: AbstractBody

    def __init__(self, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        self._my_endpoint = endpoint
        self._my_status_code = status_code
        self._my_headers = headers
        self._my_body = body

    def get_endpoint(self) -> AbstractEndpoint:
        """
        This method returns the endpoint
        :return:
        """
        return self._my_endpoint

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

class ResponseContent(AbstractContent):
    """
    This class represents a http Response.
    """
    def __init__(self, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(endpoint, status_code, headers, body)

class RequestContent(AbstractContent):
    """
    This class represents a http Request.
    """
    def __init__(self, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, body: AbstractBody) -> None:
        super().__init__(endpoint, status_code, headers, body)
