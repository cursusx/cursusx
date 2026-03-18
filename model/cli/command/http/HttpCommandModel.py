from abc import abstractmethod

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.CommandRepresentation import StringCommandFlagStrategy
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput
from model.cli.command.http.Contants import HTTP_COMMAND_NAME
from model.cli.command.http.HttpOutputModel import HttpOutput
from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.data.DataModel import AbstractHttpData, HttpDataBuilder
from model.http.info.content.ResponseModel import ResponseContent


class AbstractHttpCommand(AbstractCommand):
    _my_http_engine: AbstractHttpEngine

    def __init__(self, http_engine: AbstractHttpEngine, command_name: str):
        super().__init__(command_name, StringCommandFlagStrategy())
        self._my_http_engine = http_engine
        self._my_http_command_name = command_name

    @abstractmethod
    def execute_command(self, command: str) -> AbstractOutput:
        pass


class HttpCommand(AbstractHttpCommand):
    _my_http_data_builder: HttpDataBuilder

    def __init__(self, http_engine: AbstractHttpEngine):
        self._my_http_data_builder = HttpDataBuilder()
        super().__init__(http_engine,
                         HTTP_COMMAND_NAME)

    def execute_command(self, command: str) -> AbstractOutput:
        flags: set[AbstractFlag] = self.prepare_flags(command)
        for flag in flags:
            # given the internal value it works with the builder
            flag.get_flag_value().match_value()
        return self._execute_http_command(self._my_http_data_builder.build())

    def prepare_flags(self, command: str) -> set[AbstractFlag]:
        # TODO: for each matched flag, we store the value into it
        return self._my_flag_strategy.extract_flag_representation(command)

    def get_description(self) -> str:
        return f"Command name: {self._my_command_name}. \n" + super().get_description()

    def _execute_http_command(self, request: AbstractHttpData) -> AbstractOutput:
        response: ResponseContent = self._my_http_engine.do_query(request)
        return HttpOutput(response)
