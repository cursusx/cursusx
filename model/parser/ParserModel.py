from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.http.Contants import HTTP_COMMAND_NAME, STANDARD_ENGINE_NAME
from model.cli.command.http.HttpCommandModel import HttpCommand
from model.http.engine.Engines import get_engine

T = TypeVar('T')


def get_command_parser() -> AbstractCommand:
    return HttpCommand(http_engine=get_engine(STANDARD_ENGINE_NAME))


class AbtractParserStrategy(ABC, Generic[T]):
    @abstractmethod
    def parse_command(self, command: T) -> AbstractCommand:
        pass


class CliParserStrategy(AbtractParserStrategy[str]):
    def parse_command(self, command: str) -> AbstractCommand:
        if command == '':
            raise ValueError('Input command is empty!')
        command_and_flags: list[str] = command.split(' ')
        command_name = command_and_flags[0]

        if command_name == HTTP_COMMAND_NAME:
            return HttpCommand(http_engine=get_engine(STANDARD_ENGINE_NAME))
        raise ValueError('Command is invalid!')


class ParserFactory(Generic[T]):
    _my_strategy: AbtractParserStrategy[T]

    def __init__(self, command_parser: AbtractParserStrategy[T] = CliParserStrategy()):
        self._my_strategy = command_parser

    def from_command(self, input_command: T) -> AbstractCommand:
        return self._my_strategy.parse_command(input_command)
