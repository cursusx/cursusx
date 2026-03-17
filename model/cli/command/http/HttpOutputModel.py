from model.cli.command.OutputModel import AbstractOutput
from model.http.info.ContentModel import ResponseContent


class HttpOutput(AbstractOutput[ResponseContent, str]):
    def __init__(self, output: ResponseContent):
        super().__init__(output)

    def wrap_output(self) -> str:
        return ""
