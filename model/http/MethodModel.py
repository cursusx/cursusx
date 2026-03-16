from abc import ABC, abstractmethod
from http import HTTPMethod

from model.http.ContentModel import RequestContent, ResponseContent

# TODO: add tests


class AbstractHttpMethod(ABC):
    _my_http_method: HTTPMethod
    _my_http_request: RequestContent

    def __init__(self, method: HTTPMethod, request: RequestContent):
        self._my_http_method = method
        self._my_http_request = request

    def get_http_request(self) -> RequestContent:
        return self._my_http_request
