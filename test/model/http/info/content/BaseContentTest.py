import unittest
from abc import ABC
from http import HTTPStatus

from model.http.info.body.BodyModel import AbstractBody
from model.http.info.content.ContentModel import AbstractContent
from model.http.info.endpoint.EndpointModel import AbstractEndpoint
from model.http.info.header.HeaderModel import Headers, AbstractHeader
from model.http.info.parameter.ParameterModel import Parameters, Parameter, AbstractParameter


class BaseContentTestCase(unittest.TestCase):
    __test__ = False
    _my_endpoint: AbstractEndpoint
    _my_headers: Headers
    _my_parameters: Parameters
    _my_body: AbstractBody
    content: AbstractContent

    def __init__(self, content: AbstractContent, method_name: str = "runTest"):
        super().__init__(method_name)
        self.content = content

    def test_headers(self):
        assert all(
            header in self._my_headers.get_headers_set() for header in self.content.get_headers().get_headers_set())

    def test_parameters(self):
        assert all(
            parameter in self._my_parameters.get_parameters_set()for parameter in self.content.get_parameters().get_parameters_set())

    def test_endpoint(self):
        assert self.content.get_endpoint().dump() == self._my_endpoint.dump()

    def test_body(self):
        assert self.content.get_body().get_content() == self._my_body.get_content()
