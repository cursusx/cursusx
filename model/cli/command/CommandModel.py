from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.cli.command.CommandRepresentation import AbstractExtractCommandFlagStrategy
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput

_T = TypeVar("_T", bound=AbstractOutput)


class AbstractCommand(ABC, Generic[_T]):
    _my_command_name: str
    _my_flag_strategy: AbstractExtractCommandFlagStrategy

    def __init__(self, command_name: str, flag_strategy: AbstractExtractCommandFlagStrategy):
        self._my_command_name = command_name
        self._my_flag_strategy = flag_strategy

    @abstractmethod
    def execute_command(self, command: str) -> _T:
        """
        This method extracts from the input command all the flags, execute for each flag the logic and then it returns the output of the command
        :param command: input flag to parse
        :return: see above.
        """
        pass

    @abstractmethod
    def prepare_flags(self, command: str) -> set[AbstractFlag]:
        pass

    def get_description(self) -> str:
        """
        This method returns the description of the command.
        :return:
        """
        return "The following command supports all these flags:"
