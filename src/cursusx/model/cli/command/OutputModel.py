from abc import ABC, abstractmethod

from typing_extensions import TypeVar, Generic


_T = TypeVar("_T")


class AbstractOutput(ABC, Generic[_T]):
    """
    Wrapper for the output.
    """
    _my_output: _T

    def __init__(self, output: _T):
        self._my_output = output

    def get_output(self) -> _T:
        return self._my_output

    @abstractmethod
    def wrap_output(self) -> str:
        """
        Return a string representation of the command output.
        :return: see above.
        """
        pass
