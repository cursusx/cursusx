from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.http.Contants import HTTP_FLAG_METHOD

_I = TypeVar("_I")
_T = TypeVar("_T")


class AbstractExtractCommandFlagStrategy(ABC, Generic[_I, _T]):
    _my_query_data_builder: AbstractBuilder[_T]

    def __init__(self, my_query_data_builder: AbstractBuilder[_T]):
        self._my_query_data_builder = my_query_data_builder

    @abstractmethod
    def extract_flag_representation(self, input_command: _I) -> set[AbstractFlag]:
        pass


class StringCommandFlagStrategy(AbstractExtractCommandFlagStrategy[str, _T]):
    def __init__(self, my_query_data_builder: AbstractBuilder[_T]):
        super().__init__(my_query_data_builder)

    def extract_flag_representation(self, input_command: str, ) -> set[AbstractFlag]:
        # TODO: for each flag, match it and store the value in the flag value.
        array_of_flags: list[str] = input_command.split()[1:]
        all_flags: set[AbstractFlag] = set()
        for single_flag in array_of_flags:
            # a flag is of the type: -flag_name?(=value)
            flag_name: str = single_flag.split('-')[1]
            # TODO: create a factory for all the flags
            if flag_name == HTTP_FLAG_METHOD:
                print(1)
        return set()
