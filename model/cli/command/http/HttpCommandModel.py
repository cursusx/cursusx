from abc import abstractmethod

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput
from model.cli.command.http.Contants import HTTP_COMMAND_NAME
from model.cli.command.http.HttpOutputModel import HttpOutput
from model.cli.command.http.flags.HttpFlags import get_all_http_method_flags
from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.data.DataModel import AbstractHttpData
from model.http.info.content.ResponseModel import ResponseContent


class AbstractHttpCommand(AbstractCommand):
    _my_http_engine: AbstractHttpEngine

    def __init__(self, http_engine: AbstractHttpEngine, command_name: str, flags: set[AbstractFlag]):
        super().__init__(command_name, flags)
        self._my_http_engine = http_engine
        self._my_http_command_name = command_name

    @abstractmethod
    def execute_http_command(self, request: AbstractHttpData) -> AbstractOutput:
        pass


class HttpCommand(AbstractHttpCommand):
    def __init__(self, http_engine: AbstractHttpEngine):
        super().__init__(http_engine,
                         HTTP_COMMAND_NAME,
                         get_all_http_method_flags())

    def get_description(self) -> str:
        return f"Command name: {self._my_command_name}. \n" + super().get_description()

    def execute_http_command(self, request: AbstractHttpData) -> AbstractOutput:
        response: ResponseContent = self._my_http_engine.do_query(request)
        return HttpOutput(response)
