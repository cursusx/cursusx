from abc import ABC, abstractmethod

from typing_extensions import TypeVar, Generic

_T = TypeVar("_T")
_O = TypeVar("_O")


class AbstractOutput(ABC, Generic[_T, _O]):
    """
    Wrapper for the output.
    """
    @abstractmethod
    def wrap_output(self, output: _T) -> _O:
        pass
