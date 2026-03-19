from http import HTTPStatus

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.http.HttpCommandModel import HttpCommand
from model.cli.command.http.HttpOutputModel import HttpOutput
from model.parser.ParserModel import ParserFactory
from test.util.BaseServerTestCase import BaseServerTestCase


class ParseTest(BaseServerTestCase):
    __test__ = True

    def __init__(self, method_name: str = "runTest"):
        super().__init__('http://localhost', 8080, method_name)

    def test_should_be_possible_to_run_http_command(self) -> None:
        command: str = "http -method=get -endpoint=http://localhost:8080"
        ParserFactory[str]().from_command(
            input_command=command).execute_command(command)
