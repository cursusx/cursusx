from abc import ABC
from http import HTTPStatus
from typing import Iterable, TypeVar

from model.http.info.endpoint.EndpointModel import AbstractEndpoint
from model.http.info.body.BodyModel import AbstractBody
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters

# TODO: ADD TESTS
_SENTINEL = object()

_T = TypeVar('_T', bound=Iterable)


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

    def __init__(self, endpoint: AbstractEndpoint, headers: Headers, parameters: Parameters, body: AbstractBody):
        self._my_endpoint = endpoint
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
