from abc import ABC, abstractmethod

from model.http.engine.HttpEngineModel import AbstractHttpEngine


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
