from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from cursusx.model.cli.command.CommandModel import AbstractCommand
from cursusx.model.cli.command.http.Contants import HTTP_COMMAND_NAME, STANDARD_ENGINE_NAME
from cursusx.model.cli.command.http.HttpCommandModel import HttpCommand
from cursusx.model.http.engine.Engines import get_engine

T = TypeVar('T')


class AbtractParserStrategy(ABC, Generic[T]):
    """
    Abtract class that defines the strategy for parsing the input query of the user.
    This class allows to translate the input command of a given type into the actual command class.
    """
    @abstractmethod
    def parse_command(self, command: T) -> AbstractCommand:
        """
        Parse the input command of the user and translate it into the actual class representation.
        :param command: input command of the user to parse.
        :return: actual class implementation.
        """
        pass


class CliParserStrategy(AbtractParserStrategy[str]):
    """
    Implementation for a CLI parser strategy, this class allows to work with input string type.
    """

    def parse_command(self, command: str) -> AbstractCommand:
        if command == '':
            raise ValueError('Input command is empty!')
        command_and_flags: list[str] = command.split(' ')
        command_name = command_and_flags[0]

        if command_name == HTTP_COMMAND_NAME:
            return HttpCommand(http_engine=get_engine(STANDARD_ENGINE_NAME))
        raise ValueError('Command is invalid!')


class ParserFactory(Generic[T]):
    """
    Factory class that allows to create an instance of the parser strategy.
    In this way different implementation fo the command listener has its own implementation.

    Current supported implementation:
    1. from command line
    """
    _my_strategy: AbtractParserStrategy[T]

    def __init__(self, command_parser: AbtractParserStrategy[T] = CliParserStrategy()):
        self._my_strategy = command_parser

    def from_command(self, input_command: T) -> AbstractCommand:
        return self._my_strategy.parse_command(input_command)
