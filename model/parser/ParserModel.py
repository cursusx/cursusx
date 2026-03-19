from abc import ABC, abstractmethod
from typing import TypeVar, Generic, cast

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.OutputModel import AbstractOutput
from model.cli.command.http.Contants import HTTP_COMMAND_NAME
from model.cli.command.http.HttpCommandModel import HttpCommand
from model.cli.command.http.HttpOutputModel import HttpOutput
from model.http.engine.Engines import get_engine
from model.http.engine.StandardHttpEngineModel import STANDARD_ENGINE_NAME


_T = TypeVar("_T", bound=AbstractOutput)


class AbstractParser(ABC, Generic[_T]):
    @abstractmethod
    def _parse_command(self, input_command: str = '') -> AbstractCommand[_T]:
        pass

    def execute_command(self, command: str) -> _T:
        return (self._parse_command(command)
                .execute_command(command))


class Parser(AbstractParser[_T]):
    def _parse_command(self, input_command: str = '') -> AbstractCommand[_T]:
        if input_command == '':
            raise ValueError('Input command is empty!')
        command_and_flags: list[str] = input_command.split(' ')
        command_name = command_and_flags[0]

        if command_name == HTTP_COMMAND_NAME:
            return cast(AbstractCommand[_T], HttpCommand(get_engine(STANDARD_ENGINE_NAME)))
        raise ValueError('Command is invalid!')
