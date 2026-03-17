from abc import ABC
from http import HTTPMethod

from model.http.info.content.RequestModel import RequestContent

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
