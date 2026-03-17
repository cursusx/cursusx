from abc import ABC
from http import HTTPStatus

from model.http.info.EndpointModel import AbstractEndpoint
from model.http.info.BodyModel import AbstractBody
from model.http.info.HeaderModel import Headers
from model.http.info.ParameterModel import Parameters

# TODO: ADD TESTS
_SENTINEL = object()


class AbstractContent(ABC):
    """
    This class represents an http content.
    It has an endpoint, a status code, a collection of headers and a body.
    """
    _my_endpoint: AbstractEndpoint
    _my_status_code: HTTPStatus
    _my_headers: Headers
    _my_parameters: Parameters
    _my_body: AbstractBody

    def __init__(self, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> None:
        self._my_endpoint = endpoint
        self._my_status_code = status_code
        self._my_headers = headers
        self._my_parameters = parameters
        self._my_body = body

    def get_endpoint(self) -> AbstractEndpoint:
        """
        This method returns the endpoint.
        :return:
        """
        return self._my_endpoint

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

    def get_parameters(self) -> Parameters:
        """
        This method returns all the parameters.
        :return:
        """
        return self._my_parameters

    def get_body(self) -> AbstractBody:
        """
        This method returns the body.
        :return: see above
        """
        return self._my_body


class ResponseContent(AbstractContent):
    """
    This class represents a http Response.
    """

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> None:
        if _sentinel is _SENTINEL:
            raise TypeError(
                "In order to create a Response you have to use the factory http.")
        super().__init__(endpoint, status_code, headers, parameters, body)

    @classmethod
    def create_response(cls, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> 'ResponseContent':
        return cls(_sentinel=_SENTINEL,
                   endpoint=endpoint,
                   status_code=status_code,
                   headers=headers,
                   parameters=parameters,
                   body=body)


class RequestContent(AbstractContent):
    """
    This class represents a http Request.
    """

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> None:
        if _sentinel is _SENTINEL:
            raise TypeError(
                "In order to create a Request you have to use the factory http.")
        super().__init__(endpoint, status_code, headers, parameters, body)

    @classmethod
    def create_request(cls, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> 'RequestContent':
        return cls(_sentinel=_SENTINEL, endpoint=endpoint, status_code=status_code, headers=headers, parameters=parameters, body=body)
