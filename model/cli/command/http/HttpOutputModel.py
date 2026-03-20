from model.cli.command.OutputModel import AbstractOutput
from model.http.info.content.ResponseModel import ResponseContent


class HttpOutput(AbstractOutput[ResponseContent]):
    def __init__(self, output: ResponseContent):
        super().__init__(output)

    def wrap_output(self) -> str:
        output: str = f"Got the following status code from the command: {self.get_output().get_status_code()}\n"
        output += f"Headers:\n[ {self.get_output().get_headers()}]\n"
        output += f"Parameters:\n{self.get_output().get_parameters()}"
        return output
