from http import HTTPStatus

from model.builder.BuilderModel import AbstractBuilder
from model.http.info.BodyModel import AbstractBody
from model.http.info.content.ContentModel import AbstractContent
from model.http.info.EndpointModel import AbstractEndpoint
from model.http.info.HeaderModel import Headers
from model.http.info.ParameterModel import Parameters

_SENTINEL = object()


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


class RequestContentBuilder(AbstractBuilder[RequestContent]):
    _my_endpoint: AbstractEndpoint
    _my_status_code: HTTPStatus
    _my_headers: Headers
    _my_parameters: Parameters
    _my_body: AbstractBody

    def add_endpoint(self, endpoint: AbstractEndpoint) -> 'RequestContentBuilder':
        self._my_endpoint = endpoint
        return self

    def add_status_code(self, status_code: HTTPStatus) -> 'RequestContentBuilder':
        self._my_status_code = status_code
        return self

    def add_headers(self, headers: Headers) -> 'RequestContentBuilder':
        self._my_headers = headers
        return self

    def add_parameters(self, parameters: Parameters) -> 'RequestContentBuilder':
        self._my_parameters = parameters
        return self

    def add_body(self, body: AbstractBody) -> 'RequestContentBuilder':
        self._my_body = body
        return self

    def build(self) -> RequestContent:
        if self._my_endpoint and self._my_status_code and self._my_headers and self._my_parameters and self._my_body:
            return RequestContent.create_request(endpoint=self._my_endpoint,
                                                 status_code=self._my_status_code,
                                                 headers=self._my_headers,
                                                 parameters=self._my_parameters,
                                                 body=self._my_body)
        raise TypeError(
            "In order to build the Request all the parameters has to be set.")
