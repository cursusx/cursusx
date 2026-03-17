from abc import ABC, abstractmethod
from re import Pattern

from typing_extensions import TypeVar

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.OutputModel import AbstractOutput

_V = TypeVar("_V")


class AbstractFlagLogic(ABC):
    @abstractmethod
    def apply_flag_logic(self, command: AbstractCommand) -> AbstractOutput:
        pass


class AbstractFlagValue(ABC):
    _my_representation: Pattern

    def is_valid_flag_value(self, flag_value: str) -> bool:
        """
        This method allows to check if the flag is valid.
        :param flag_value: input string that represent the flag value
        :return: see above
        """
        return self._my_representation.match(flag_value) is not None


class AbstractFlag(ABC):
    """
    This class represents a specific command flag, defined in this way:
    -name=value
    """
    _my_name: str
    _my_logic: AbstractFlagLogic
    _my_flag_values: AbstractFlagValue

    def __init__(self, my_name: str, my_logic: AbstractFlagLogic):
        self._my_name = my_name
        self._my_logic = my_logic

    @abstractmethod
    def get_flag_descritpion(self) -> str:
        pass

    def __repr__(self) -> str:
        return f"{self._my_name}: {self.get_flag_descritpion()}"
