from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_T = TypeVar("_T")


class AbstractBuilder(ABC, Generic[_T]):
    @abstractmethod
    def build(self) -> _T:
        pass
