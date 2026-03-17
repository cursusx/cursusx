from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.builder.BuilderModel import AbstractBuilder
from model.http.info.ContentModel import AbstractContent

_T = TypeVar("_T", bound=AbstractContent)


class AbstractQueryBuilder(ABC, Generic[_T]):
    _my_builder: AbstractBuilder[_T]

    @abstractmethod
    def build(self) -> _T:
        pass
