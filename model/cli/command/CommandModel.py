from abc import ABC, abstractmethod

from model.cli.command.CommandRepresentation import AbstractExtractCommandFlagStrategy
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput


class AbstractCommand(ABC):
    _my_command_name: str
    _my_flags: set[AbstractFlag]
    _my_flag_strategy: AbstractExtractCommandFlagStrategy

    def __init__(self, command_name: str, flags: set[AbstractFlag], flag_strategy: AbstractExtractCommandFlagStrategy):
        self._my_command_name = command_name
        self._my_flags = set(flags)
        self._my_flag_strategy = flag_strategy

    @abstractmethod
    def execute_command(self, command: str) -> AbstractOutput:
        """
        This method extracts from the input command all the flags, execute for each flag the logic and then it returns the output of the command
        :param command: input flag to parse
        :return: see above.
        """
        pass

    def get_description(self) -> str:
        """
        This method returns the description of the command.
        :return:
        """
        output: str = "The following command supports all these flags:"
        for flag in self._my_flags:
            output += f"{flag.get_flag_descritpion()}\n"
        return output
