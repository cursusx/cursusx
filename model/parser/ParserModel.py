from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.http.Contants import HTTP_COMMAND_NAME, STANDARD_ENGINE_NAME
from model.cli.command.http.HttpCommandModel import HttpCommand
from model.http.engine.Engines import get_engine


def get_command_parser() -> AbstractCommand:
    return HttpCommand(http_engine=get_engine(STANDARD_ENGINE_NAME))


class ParserFactory:
    @staticmethod
    def from_command(input_command: str) -> AbstractCommand:
        if input_command == '':
            raise ValueError('Input command is empty!')
        command_and_flags: list[str] = input_command.split(' ')
        command_name = command_and_flags[0]

        if command_name == HTTP_COMMAND_NAME:
            return get_command_parser()
        raise ValueError('Command is invalid!')
