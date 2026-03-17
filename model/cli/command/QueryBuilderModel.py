from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.CommandModel import AbstractCommand

_T = TypeVar("_T", bound=AbstractCommand)


class AbstractQueryBuilder(ABC, Generic[_T]):
    _my_builder: AbstractBuilder[_T]

    @abstractmethod
    def build(self) -> _T:
        pass
