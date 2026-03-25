from abc import abstractmethod

from cursusx.model.cli.command.CommandModel import AbstractCommand
from cursusx.model.cli.command.CommandRepresentation import StringCommandFlagStrategy
from cursusx.model.cli.command.FlagModel import AbstractFlag
from cursusx.model.cli.command.http.Contants import HTTP_COMMAND_NAME
from cursusx.model.cli.command.http.HttpOutputModel import HttpOutput
from cursusx.model.cli.command.http.flags.HttpFlagsFactory import HttpFlagFactory
from cursusx.model.http.engine.HttpEngineModel import AbstractHttpEngine
from cursusx.model.http.info.data.DataModel import AbstractHttpData, HttpDataBuilder
from cursusx.model.http.info.content.ResponseModel import ResponseContent


class AbstractHttpCommand(AbstractCommand[HttpOutput]):
    """
    This class represent the definition of an http command, it works with the HttpOutput class.

    An example of this class from cli is: http ...
    In order to work this class uses the HttpDataBuilder class for creating the input data for the query and it returns
    output wrapped in the HttpOutput class.
    """
    _my_http_engine: AbstractHttpEngine
    _my_http_data_builder: HttpDataBuilder

    def __init__(self, http_engine: AbstractHttpEngine, command_name: str):
        self._my_http_data_builder = HttpDataBuilder()
        self._my_http_engine = http_engine
        self._my_http_command_name = command_name

        super().__init__(command_name, StringCommandFlagStrategy(
            self._my_http_data_builder, HttpFlagFactory()))

    @abstractmethod
    def execute_command(self, command: str) -> HttpOutput:
        pass


class HttpCommand(AbstractHttpCommand):
    """
    Actual implementation of the Http command class.
    """

    def __init__(self, http_engine: AbstractHttpEngine):
        super().__init__(http_engine,
                         HTTP_COMMAND_NAME)

    def execute_command(self, command: str) -> HttpOutput:
        flags: set[AbstractFlag] = self.prepare_flags(command)
        for flag in flags:
            # given the internal value it works with the builder
            flag.get_flag_value().match_value()
        return self._execute_http_command(self._my_http_data_builder.build())

    def prepare_flags(self, command: str) -> set[AbstractFlag]:
        """
        This method allows to extract end create all the defined flags in the input command.
        :param command: input command where all the flags are specified.
        :return: the set of all defined flags.
        """
        return self._my_flag_strategy.extract_flag_representation(command)

    def get_description(self) -> str:
        return f"Command name: {self._my_command_name}. \n" + super().get_description()

    def _execute_http_command(self, request: AbstractHttpData) -> HttpOutput:
        """
        This method allows to execute the http command.
        :param request: input request created from the input flags.
        :return: the output of the http command.
        """
        response: ResponseContent = self._my_http_engine.do_query(request)
        return HttpOutput(response)
