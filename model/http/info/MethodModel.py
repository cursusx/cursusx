from abc import ABC
from http import HTTPMethod

from model.http.info.content.RequestModel import RequestContent


# TODO: add tests


class AbstractHttpMethod(ABC):
    _my_http_method: HTTPMethod
    _my_http_request: RequestContent

    def __init__(self, method: HTTPMethod, request: RequestContent):
        self._my_http_method = method
        self._my_http_request = request

    def get_http_request(self) -> RequestContent:
        return self._my_http_request

    def get_http_method(self) -> HTTPMethod:
        return self._my_http_method


class HttpMethod(AbstractHttpMethod):
    def __init__(self, method: HTTPMethod, request: RequestContent):
        super().__init__(method, request)
