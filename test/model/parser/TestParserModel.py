from model.parser.ParserModel import AbstractParser, Parser
from test.mock.ServerMock import start_mock_server, kill_mock_server
from test.util.BaseServerTestCase import BaseServerTestCase


class ParseTest(BaseServerTestCase):
    __test__ = True

    def __init__(self):
        super().__init__('localhost', 8080)

    def test_should_be_possible_to_run_http_command(self) -> None:
        command: str = "http -method=get -endpoint=localhost:8080"
        parser: AbstractParser = Parser()
        parser.execute_command(command)
