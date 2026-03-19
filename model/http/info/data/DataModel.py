from abc import ABC
from http import HTTPMethod

from model.builder.BuilderModel import AbstractBuilder
from model.http.info.body.BodyModel import AbstractBody, Body
from model.http.info.content.RequestModel import RequestContent
from model.http.info.endpoint.EndpointModel import AbstractEndpoint, BasicEndpoint
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters

_SENTINEL = object()


class AbstractHttpData(ABC):
    _my_http_method: HTTPMethod
    _my_http_request: RequestContent

    def __init__(self, method: HTTPMethod, request: RequestContent):
        self._my_http_method = method
        self._my_http_request = request

    def get_http_request(self) -> RequestContent:
        return self._my_http_request

    def get_http_method(self) -> HTTPMethod:
        return self._my_http_method


class HttpData(AbstractHttpData):
    def __init__(self, _sentinel: object = None, *, method: HTTPMethod, request: RequestContent):
        if _sentinel is None:
            raise TypeError(
                "In order to create this class you have to use the factory method.")
        super().__init__(method, request)

    @classmethod
    def create_data(cls, method: HTTPMethod, request: RequestContent):
        if method is None or request is None:
            raise ValueError("The input parameters cannot be None.")
        return cls(_sentinel=_SENTINEL, method=method, request=request)


class HttpDataBuilder(AbstractBuilder[HttpData]):
    _my_endpoint: AbstractEndpoint | None
    _my_headers: Headers = Headers.empty()
    _my_parameters: Parameters = Parameters.empty()
    _my_body: AbstractBody = Body.empty()
    _my_http_method: HTTPMethod | None

    def __init__(self):
        self._my_endpoint: AbstractEndpoint | None = BasicEndpoint.create_endpoint(
            'localhost', 1)
        self._my_headers: Headers = Headers.empty()
        self._my_parameters: Parameters = Parameters.empty()
        self._my_body: AbstractBody = Body.empty()
        self._my_http_method: HTTPMethod | None = None

    def add_http_method(self, method: HTTPMethod) -> 'HttpDataBuilder':
        self._my_http_method = method
        return self

    def add_endpoint(self, endpoint: AbstractEndpoint) -> 'HttpDataBuilder':
        self._my_endpoint = endpoint
        return self

    def add_headers(self, headers: Headers) -> 'HttpDataBuilder':
        self._my_headers = headers
        return self

    def add_parameters(self, parameters: Parameters) -> 'HttpDataBuilder':
        self._my_parameters = parameters
        return self

    def add_body(self, body: AbstractBody) -> 'HttpDataBuilder':
        self._my_body = body
        return self

    def build(self) -> HttpData:
        if self._my_http_method and self._my_headers and self._my_parameters and self._my_body and self._my_endpoint:
            return HttpData.create_data(self._my_http_method, RequestContent.create_request(endpoint=self._my_endpoint,
                                                                                            headers=self._my_headers,
                                                                                            parameters=self._my_parameters,
                                                                                            body=self._my_body))
        raise TypeError(
            "In order to create a HttpData class you have to specify all the parameters")
