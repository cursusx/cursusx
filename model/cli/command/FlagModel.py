from abc import ABC, abstractmethod
from re import Pattern
from typing import Generic, NoReturn

from typing_extensions import TypeVar

from model.cli.command.QueryBuilderModel import AbstractQueryBuilder

_T = TypeVar("_T", bound=AbstractQueryBuilder)

# TODO: at each command, create a new query builder and pass it to each flag value


class AbstractFlagValue(ABC, Generic[_T]):
    """
    This class represent the value of a flag, so what is after the equal in the flag definition.
    -myflag=value <- this
    """
    _my_query_builder: _T
    _my_representation: Pattern

    def __init__(self, my_query_builder: _T):
        self._my_query_builder = my_query_builder

    def is_valid_flag_value(self, flag_value: str) -> bool:
        """
        This method allows to check if the flag is valid.
        :param flag_value: input string that represent the flag value
        :return: see above
        """
        return self._my_representation.match(flag_value) is not None

    @abstractmethod
    def match_value(self, flag_value: str) -> None:
        pass


class AbstractFlag(ABC, Generic[_T]):
    """
    This class represents a specific command flag, defined in this way:
    -name=value
    """
    _my_name: str
    _my_flag_value: AbstractFlagValue[_T]

    def __init__(self, my_name: str, my_flag_value: AbstractFlagValue[_T]):
        self._my_name = my_name
        self._my_flag_value = my_flag_value

    @abstractmethod
    def get_flag_descritpion(self) -> str:
        pass

    def __repr__(self) -> str:
        return f"{self._my_name}: {self.get_flag_descritpion()}"
