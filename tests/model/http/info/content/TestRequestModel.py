from http import HTTPStatus

from model.http.info.body.BodyModel import Body, AbstractBody
from model.http.info.content.RequestModel import RequestContent
from model.http.info.cookie.CookieModel import Cookies
from model.http.info.endpoint.EndpointModel import AbstractEndpoint, BasicEndpoint
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters, Parameter
from tests.model.http.info.content.BaseContentTest import BaseContentTestCase


class TestRequest(BaseContentTestCase):
    __test__ = True
    _my_endpoint: AbstractEndpoint
    _my_headers: Headers
    _my_parameters: Parameters
    _my_cookies: Cookies
    _my_body: AbstractBody

    def __init__(self, method: str = "runTest"):
        self._my_endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
            'localhost', 8080)
        self._my_headers: Headers = Headers.from_dictionary(
            {'content-type': 'application/json'})
        self._my_parameters: Parameters = Parameters.from_list(
            [Parameter.from_tuple(('key', 'value'))])
        self._my_body: AbstractBody = Body.from_string("random")
        self._my_cookies: Cookies = Cookies.from_string_collection(
            [('key', 'value')])

        super().__init__(RequestContent.create_request(endpoint=self._my_endpoint,
                                                       headers=self._my_headers,
                                                       parameters=self._my_parameters,
                                                       cookies=self._my_cookies,
                                                       body=self._my_body
                                                       ), method)
