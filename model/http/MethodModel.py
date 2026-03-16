from abc import ABC, abstractmethod

from model.http.ContentModel import RequestContent, ResponseContent


class AbstractHttpMethod(ABC):
    @abstractmethod
    def do_method(self, request: RequestContent) -> ResponseContent:
        pass