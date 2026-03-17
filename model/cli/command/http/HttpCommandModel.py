from abc import abstractmethod

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput, HttpOutput
from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.ContentModel import ResponseContent
from model.http.info.MethodModel import AbstractHttpMethod


class AbstractHttpCommand(AbstractCommand):
    _my_http_engine: AbstractHttpEngine
    # TODO: Create a request builder that is shared among some of the flags

    def __init__(self, http_engine: AbstractHttpEngine, command_name: str, flags: set[AbstractFlag]):
        super().__init__(command_name, flags)
        self._my_http_engine = http_engine

    @abstractmethod
    def execute_http_command(self, request: AbstractHttpMethod) -> AbstractOutput:
        pass


class HttpCommand(AbstractHttpCommand):
    _http_command_name: str = "http"

    def __init__(self, http_engine: AbstractHttpEngine, flags: set[AbstractFlag]):
        super().__init__(http_engine, self._http_command_name, flags)

    def get_description(self) -> str:
        return f"Command name: {self._my_command_name}. \n" + super().get_description()

    def execute_http_command(self, request: AbstractHttpMethod) -> AbstractOutput:
        response: ResponseContent = self._my_http_engine.do_query(request)
        return HttpOutput(response)
