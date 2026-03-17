from abc import ABC, abstractmethod

from model.cli.command.CommandModel import AbstractCommand
from model.cli.command.OutputModel import AbstractOutput


class AbstractFlagLogic(ABC):
    @abstractmethod
    def apply_flag_logic(self, command: AbstractCommand) -> AbstractOutput:
        pass


class AbstractFlag(ABC):
    _my_name: str
    _my_logic: AbstractFlagLogic

    def __init__(self, my_name: str, my_logic: AbstractFlagLogic):
        self._my_name = my_name
        self._my_logic = my_logic
