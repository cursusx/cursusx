from abc import ABC, abstractmethod

from model.http.info.ContentModel import ResponseContent
from model.http.info.MethodModel import AbstractHttpMethod


class AbstractEngine(ABC):
    """
    This is the engine for making all the http requests
    """
    _my_engine_name: str

    def __init__(self, my_engine_name: str):
        self._my_engine_name = my_engine_name

    @abstractmethod
    def do_query(self, http_request: AbstractHttpMethod) -> ResponseContent:
        pass
