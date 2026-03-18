from model.parser.ParserModel import AbstractParser, Parser


def test_should_be_possible_to_run_http_command():
    command: str = "http -method=get"
    parser: AbstractParser = Parser()
    parser.execute_command(command)
