from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.cli.command.FlagModel import AbstractFlag

_I = TypeVar("_I")


class AbstractExtractCommandFlagStrategy(ABC, Generic[_I]):
    @abstractmethod
    def extract_flag_representation(self, input_command: _I) -> set[AbstractFlag]:
        pass


class StringCommandFlagStrategy(AbstractExtractCommandFlagStrategy[str]):
    def extract_flag_representation(self, input_command: str) -> set[AbstractFlag]:
        return set()
