from abc import ABC, abstractmethod

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.http.Contants import HTTP_COMMAND_NAME
from model.cli.command.http.HttpCommandModel import HttpCommand
from model.http.engine.Engines import get_engine
from model.http.engine.StandardHttpEngineModel import STANDARD_ENGINE_NAME


class AbstractParser(ABC):
    @abstractmethod
    def parse_command(self, input_command: str = '') -> AbstractCommand:
        pass


class Parser(AbstractParser):
    def parse_command(self, input_command: str = '') -> AbstractCommand:
        if input_command == '':
            raise ValueError('Input command is empty!')
        command_and_flags: list[str] = input_command.split(' ')[1:]
        command_name = command_and_flags[0]

        if command_name == HTTP_COMMAND_NAME:
            return HttpCommand(get_engine(STANDARD_ENGINE_NAME))
        raise ValueError('Command is invalid!')
