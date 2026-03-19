from model.parser.ParserModel import AbstractParser, Parser
from test.mock.ServerMock import start_mock_server


def test_should_be_possible_to_run_http_command():
    server = start_mock_server('localhost', 8080)
    command: str = "http -method=get -endpoint=localhost:8080"
    parser: AbstractParser = Parser()
    parser.execute_command(command)
    server.server_close()
