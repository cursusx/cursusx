from abc import ABC, abstractmethod

from model.cli.command.OutputModel import AbstractOutput
from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.info.MethodModel import AbstractHttpMethod


class AbstractCommand(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """
        This method returns the description of the command.
        :return:
        """
        pass


class AbstractHttpCommand(AbstractCommand):
    _my_http_engine: AbstractHttpEngine

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def execute_http_command(self, request: AbstractHttpMethod) -> AbstractOutput:
        pass
