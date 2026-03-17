from http import HTTPStatus

import requests
from requests import Response

from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.BodyModel import Body
from model.http.info.HeaderModel import Headers
from model.http.info.MethodModel import AbstractHttpMethod
from model.http.info.ParameterModel import Parameters
from model.http.info.content.ResponseModel import ResponseContent


class StandardHttpEngine(AbstractHttpEngine):
    def __init__(self):
        super().__init__('requests')

    def _do_get(self, http_request: AbstractHttpMethod) -> ResponseContent:
        return self._execute_request(http_request.get_http_method(),
                                     http_request)

    def _do_post(self, http_request: AbstractHttpMethod) -> ResponseContent:
        return self._execute_request(http_request.get_http_method(),
                                     http_request)

    def _do_put(self, http_request: AbstractHttpMethod) -> ResponseContent:
        return self._execute_request(http_request.get_http_method(),
                                     http_request)

    def _do_delete(self, http_request: AbstractHttpMethod) -> ResponseContent:
        return self._execute_request(http_request.get_http_method(), http_request)

    def _do_patch(self, http_request: AbstractHttpMethod) -> ResponseContent:
        return self._execute_request(http_request.get_http_method(), http_request)

    def _execute_request(self, method: str, request: AbstractHttpMethod) -> ResponseContent:
        response: Response = requests.request(method=method,
                                              url=request.get_http_request().get_endpoint().dump(),
                                              params=request.get_http_request().get_parameters().dump(),
                                              headers=request.get_http_request().get_headers().dump(),
                                              data=request.get_http_request().get_body().get_content())
        return ResponseContent.create_response(endpoint=request.get_http_request().get_endpoint(),
                                               status_code=HTTPStatus(
                                                   response.status_code),
                                               headers=Headers.from_dictionary(
                                                   response.headers),
                                               parameters=Parameters.from_list(
                                                   []),
                                               body=Body.from_string(response.text))
