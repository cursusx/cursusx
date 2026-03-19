from model.parser.ParserModel import AbstractParser, Parser
from test.util.BaseServerTestCase import BaseServerTestCase


class ParseTest(BaseServerTestCase):
    __test__ = True

    def __init__(self, method_name: str = "runTest"):
        super().__init__('http://localhost', 8080, method_name)

    def test_should_be_possible_to_run_http_command(self) -> None:
        command: str = "http -method=get -endpoint=http://localhost:8080"
        parser: AbstractParser = Parser()
        parser.execute_command(command)
