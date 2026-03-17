from abc import ABC, abstractmethod

from typing_extensions import TypeVar, Generic

from model.http.info.ContentModel import ResponseContent

_T = TypeVar("_T")
_O = TypeVar("_O")


class AbstractOutput(ABC, Generic[_T, _O]):
    """
    Wrapper for the output.
    """
    @abstractmethod
    def wrap_output(self, output: _T) -> _O:
        pass


class HttpOutput(AbstractOutput[ResponseContent, str]):
    def wrap_output(self, output: ResponseContent) -> str:
        return ""
