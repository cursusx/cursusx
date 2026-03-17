from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.http.info.data.DataModel import AbstractHttpData

_B = TypeVar("_B")


class AbstractEngine(ABC, Generic[_B]):
    @abstractmethod
    def analyze(self, request: AbstractHttpData) -> _B:
        pass
