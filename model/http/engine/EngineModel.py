from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from model.http.info.MethodModel import AbstractHttpMethod

_B: TypeVar = TypeVar("_B")


class AbstractEngine(ABC):
    @abstractmethod
    def analyze[_B](self, request: AbstractHttpMethod) -> _B:
        pass
