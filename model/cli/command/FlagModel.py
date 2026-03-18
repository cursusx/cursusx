from abc import ABC, abstractmethod
from re import Pattern
from typing import Generic, NoReturn

from typing_extensions import TypeVar

from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.http.Contants import HTTP_FLAG_METHOD
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue

_T = TypeVar("_T", bound=AbstractBuilder)

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

    def __init__(self, my_name: str, my_flag_value: AbstractFlagValue[_T]):
        self._my_name = my_name
        self._my_flag_value = my_flag_value

    @abstractmethod
    def get_flag_descritpion(self) -> str:
        pass

    def get_flag_value(self) -> AbstractFlagValue[_T]:
        return self._my_flag_value

    def __repr__(self) -> str:
        return f"{self._my_name}: {self.get_flag_descritpion()}"


def _create_flag(flag_class: type[AbstractFlag],
                 flag_value: type[AbstractFlagValue],
                 flag_name: str,
                 builder: AbstractBuilder) -> AbstractFlag:
    return flag_class(my_name=flag_name, my_flag_value=flag_value(my_query_builder=builder))


class FlagFactory:
    _my_flags: dict[str, tuple[type[AbstractFlag], type[AbstractFlagValue]]] = {
        HTTP_FLAG_METHOD: (HttpMethodFlag, HttpMethodFlagValue),
    }

    @staticmethod
    def create_flag(flag_name: str, builder: AbstractBuilder) -> AbstractFlag[_T]:
        if flag_name not in FlagFactory._my_flags:
            raise KeyError(
                f"{flag_name} not exist, specify the correct flagf name.")
        return _create_flag(flag_class=FlagFactory._my_flags[flag_name][0],
                            flag_value=FlagFactory._my_flags[flag_name][1],
                            flag_name=flag_name,
                            builder=builder)
