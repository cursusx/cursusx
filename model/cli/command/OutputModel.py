from abc import ABC, abstractmethod

from typing_extensions import TypeVar, Generic

from model.http.info.ContentModel import ResponseContent

_T = TypeVar("_T")
_O = TypeVar("_O")


class AbstractOutput(ABC, Generic[_T, _O]):
    """
    Wrapper for the output.
    """
    _my_output: _T

    def __init__(self, output: _T):
        self._my_output = output

    @abstractmethod
    def wrap_output(self) -> _O:
        """
        Return a string representation of the command output.
        :return: see above.
        """
        pass
