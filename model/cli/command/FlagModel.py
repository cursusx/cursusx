from abc import ABC, abstractmethod
from re import Pattern
from typing import Generic, NoReturn

from typing_extensions import TypeVar

from model.builder.BuilderModel import AbstractBuilder

_T = TypeVar("_T", bound=AbstractBuilder)

# TODO: at each command, create a new query builder and pass it to each flag value


class AbstractFlagValue(ABC, Generic[_T]):
    """
    This class represent the value of a flag, so what is after the equal in the flag definition.
    -myflag=value <- this
    """
    _my_query_builder: _T
    _my_representation: Pattern
    _my_flag_value: str

    def __init__(self, my_query_builder: _T, flag_value: str):
        self._my_query_builder = my_query_builder
        self._my_flag_value = flag_value

    def is_valid_flag_value(self, flag_value: str) -> bool:
        """
        This method allows to check if the flag is valid.
        :param flag_value: input string that represent the flag value
        :return: see above
        """
        # TODO: Here then extract the value
        return self._my_representation.match(flag_value) is not None

    @abstractmethod
    def match_value(self) -> None:
        """
        This method takes from the internal flag value the flag value specified by the user and does something
        with the internal builder.
        :return: see above.
        """
        pass


class AbstractFlag(ABC, Generic[_T]):
    """
    This class represents a specific command flag, defined in this way:
    -name=value
    """
    _my_name: str
    _my_flag_value: AbstractFlagValue[_T]

    def __init__(self, my_flag_value: AbstractFlagValue[_T]):
        self._my_flag_value = my_flag_value

    @abstractmethod
    def get_flag_descritpion(self) -> str:
        pass

    def get_flag_value(self) -> AbstractFlagValue[_T]:
        return self._my_flag_value

    def __repr__(self) -> str:
        return f"{self._my_name}: {self.get_flag_descritpion()}"
