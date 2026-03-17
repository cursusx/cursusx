from abc import ABC

from model.cli.command.FlagModel import AbstractFlag


class AbstractCommand(ABC):
    _my_command_name: str
    _my_flags: set[AbstractFlag]

    def __init__(self, command_name: str, flags: set[AbstractFlag]):
        self._my_command_name = command_name
        self._my_flags = set(flags)

    def get_description(self) -> str:
        """
        This method returns the description of the command.
        :return:
        """
        output: str = "The following command supports all these flags:"
        for flag in self._my_flags:
            output += f"{flag.get_flag_descritpion()}\n"
        return output
