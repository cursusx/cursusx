from abc import abstractmethod
from http import HTTPMethod

from cursusx.model.http.engine.EngineModel import AbstractEngine
from cursusx.model.http.info.data.DataModel import AbstractHttpData
from cursusx.model.http.info.content.ResponseModel import ResponseContent


class AbstractHttpEngine(AbstractEngine[ResponseContent]):
    """
    This is the engine for making all the http requests
    """
    _my_engine_name: str

    def __init__(self, my_engine_name: str):
        self._my_engine_name = my_engine_name

    def get_engine_name(self) -> str:
        return self._my_engine_name

    def analyze(self, request: AbstractHttpData) -> ResponseContent:
        return self.do_query(request)

    def do_query(self, http_request: AbstractHttpData) -> ResponseContent:
        match http_request.get_http_method():
            case HTTPMethod.GET:
                return self._do_get(http_request)
            case HTTPMethod.POST:
                return self._do_post(http_request)
            case HTTPMethod.PUT:
                return self._do_put(http_request)
            case HTTPMethod.DELETE:
                return self._do_delete(http_request)
            case HTTPMethod.PATCH:
                return self._do_patch(http_request)
            case not_supported:
                raise ValueError(
                    f"The input http method: {not_supported} is not supported.")

    @abstractmethod
    def _do_get(self, http_request: AbstractHttpData) -> ResponseContent:
        pass

    @abstractmethod
    def _do_post(self, http_request: AbstractHttpData) -> ResponseContent:
        pass

    @abstractmethod
    def _do_put(self, http_request: AbstractHttpData) -> ResponseContent:
        pass

    @abstractmethod
    def _do_delete(self, http_request: AbstractHttpData) -> ResponseContent:
        pass

    @abstractmethod
    def _do_patch(self, http_request: AbstractHttpData) -> ResponseContent:
        pass
