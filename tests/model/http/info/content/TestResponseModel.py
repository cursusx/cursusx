from http import HTTPStatus

from model.http.info.body.BodyModel import AbstractBody, Body
from model.http.info.content.ResponseModel import ResponseContent
from model.http.info.endpoint.EndpointModel import AbstractEndpoint, BasicEndpoint
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters, Parameter
from tests.model.http.info.content.BaseContentTest import BaseContentTestCase


class TestResponse(BaseContentTestCase):
    __test__ = True
    _my_endpoint: AbstractEndpoint
    _my_headers: Headers
    _my_parameters: Parameters
    _my_body: AbstractBody
    _my_status_code: HTTPStatus

    def __init__(self, method: str = "runTest"):
        self._my_endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
            'localhost', 8080)
        self._my_headers: Headers = Headers.from_dictionary(
            {'content-type': 'application/json'})
        self._my_parameters: Parameters = Parameters.from_list(
            [Parameter.from_tuple(('key', 'value'))])
        self._my_body: AbstractBody = Body.from_string("random")
        self._my_status_code = HTTPStatus.OK

        super().__init__(ResponseContent.create_response(endpoint=self._my_endpoint,
                                                         status_code=self._my_status_code,
                                                         headers=self._my_headers,
                                                         parameters=self._my_parameters,
                                                         body=self._my_body
                                                         ), method)

    def test_status_code(self):
        assert self._my_status_code == HTTPStatus.OK
