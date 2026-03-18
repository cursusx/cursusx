from abc import ABC

from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue


def create_flag(flag_class: type[AbstractFlag],
                flag_value: type[AbstractFlagValue],
                flag_name: str,
                builder: AbstractBuilder) -> AbstractFlag:
    return flag_class(my_name=flag_name, my_flag_value=flag_value(my_query_builder=builder))


class AbstractFlagFactory(ABC):
    _my_flags: dict[str, tuple[type[AbstractFlag], type[AbstractFlagValue]]]

    def create_flag(self, flag_name: str, builder: AbstractBuilder) -> AbstractFlag:
        if flag_name not in self._my_flags:
            raise KeyError(
                f"{flag_name} not exist, specify the correct flagf name.")
        return create_flag(flag_class=self._my_flags[flag_name][0],
                           flag_value=self._my_flags[flag_name][1],
                           flag_name=flag_name,
                           builder=builder)
