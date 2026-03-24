from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_T = TypeVar('_T')


class IterableContent(ABC, Generic[_T]):
    """
    Rerpesents a content that can be iterated over.
    """
    @abstractmethod
    def dump(self) -> _T:
        """
        Translate the input collection into another type.
        :return: see above.
        """
        pass
