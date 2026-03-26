
from model.builder.BuilderModel import AbstractBuilder
from model.http.info.body.BodyModel import AbstractBody
from model.http.info.content.ContentModel import AbstractContent
from model.http.info.cookie.CookieModel import Cookies
from model.http.info.endpoint.EndpointModel import AbstractEndpoint
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters

_SENTINEL = object()


class RequestContent(AbstractContent):
    """
    This class represents http Request.
    """

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, headers: Headers, parameters: Parameters, cookies: Cookies, body: AbstractBody):
        if _sentinel is None:
            raise TypeError(
                "In order to create a Request you have to use the factory http.")
        super().__init__(endpoint, headers, parameters, cookies, body)

    @classmethod
    def create_request(cls, endpoint: AbstractEndpoint, headers: Headers, parameters: Parameters, cookies: Cookies, body: AbstractBody) -> 'RequestContent':
        return cls(_sentinel=_SENTINEL, endpoint=endpoint, headers=headers, parameters=parameters, cookies=cookies, body=body)


class RequestContentBuilder(AbstractBuilder[RequestContent]):
    _my_endpoint: AbstractEndpoint
    _my_headers: Headers
    _my_parameters: Parameters
    _my_cookies: Cookies
    _my_body: AbstractBody

    def add_endpoint(self, endpoint: AbstractEndpoint) -> 'RequestContentBuilder':
        self._my_endpoint = endpoint
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
        if self._my_endpoint and self._my_headers and self._my_parameters and self._my_body:
            return RequestContent.create_request(endpoint=self._my_endpoint,
                                                 headers=self._my_headers,
                                                 parameters=self._my_parameters,
                                                 cookies=self._my_cookies,
                                                 body=self._my_body)
        raise TypeError(
            "In order to build the Request all the parameters has to be set.")
