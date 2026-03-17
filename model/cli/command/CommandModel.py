from abc import ABC, abstractmethod

from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.OutputModel import AbstractOutput
from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.MethodModel import AbstractHttpMethod


class AbstractCommand(ABC):
    _my_command_name: str
    _my_flags: dict[str, AbstractFlag]

    def __init__(self, command_name: str, flags: dict[str, AbstractFlag]):
        self._my_command_name = command_name
        self._my_flags = dict(flags)

    @abstractmethod
    def get_description(self) -> str:
        """
        This method returns the description of the command.
        :return:
        """
        pass


class AbstractHttpCommand(AbstractCommand):
    _my_http_engine: AbstractHttpEngine

    def __init__(self, http_engine: AbstractHttpEngine, command_name: str, flags: dict[str, AbstractFlag]):
        super().__init__(command_name, flags)
        self._my_http_engine = http_engine

    @abstractmethod
    def execute_http_command(self, request: AbstractHttpMethod) -> AbstractOutput:
        pass
