import re
from abc import ABC, abstractmethod
from re import Pattern
from typing import TypeVar, Generic


from cursusx.model.builder.BuilderModel import AbstractBuilder
from cursusx.model.cli.command.FlagFactory import AbstractFlagFactory
from cursusx.model.cli.command.FlagModel import AbstractFlag

_I = TypeVar("_I")
_T = TypeVar("_T")


class AbstractExtractCommandFlagStrategy(ABC, Generic[_I, _T]):
    _my_query_data_builder: AbstractBuilder[_T]
    _my_flag_factory: AbstractFlagFactory

    def __init__(self, my_query_data_builder: AbstractBuilder[_T],
                 flag_factory: AbstractFlagFactory):
        self._my_query_data_builder = my_query_data_builder
        self._my_flag_factory = flag_factory

    @abstractmethod
    def extract_flag_representation(self, input_command: _I,
                                    ) -> set[AbstractFlag]:
        pass


class StringCommandFlagStrategy(AbstractExtractCommandFlagStrategy[str, _T]):
    _my_flag_with_value_regex: Pattern[str] = re.compile(
        r'-(\w+)(?:=(.+?))?(?=\s+-\w|$)', re.DOTALL)

    def __init__(self, my_query_data_builder: AbstractBuilder[_T],
                 flag_factory: AbstractFlagFactory):
        super().__init__(my_query_data_builder, flag_factory)

    def extract_flag_representation(self, input_command: str,
                                    ) -> set[AbstractFlag]:
        rest: str = input_command.split(
            None, 1)[1] if ' ' in input_command else ''
        all_flags: set[AbstractFlag] = set()
        for matches in self._my_flag_with_value_regex.finditer(rest):
            if matches:
                flag_value: str = matches.group(2) if matches.group(2) else ''
                all_flags.add(self._my_flag_factory.create_flag(
                    matches.group(1), flag_value, self._my_query_data_builder))
        return all_flags
