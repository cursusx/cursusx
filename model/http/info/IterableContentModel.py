from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_T = TypeVar('_T')


class IterableContent(ABC, Generic[_T]):
    @abstractmethod
    def dump(self) -> _T:
        pass
