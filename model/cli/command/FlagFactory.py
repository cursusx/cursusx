from abc import ABC

from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue


def create_flag(flag_class: type[AbstractFlag],
                flag_value_class: type[AbstractFlagValue],
                flag_value: str,
                builder: AbstractBuilder) -> AbstractFlag:
    return flag_class(my_flag_value=flag_value_class(my_query_builder=builder, flag_value=flag_value))


class AbstractFlagFactory(ABC):
    _my_flags: dict[str, tuple[type[AbstractFlag],
                               type[AbstractFlagValue],
                               str]
                    ]

    def create_flag(self, flag_name: str,
                    flag_value: str,
                    builder: AbstractBuilder) -> AbstractFlag:
        if flag_name not in self._my_flags:
            raise KeyError(
                f"{flag_name} not exist, specify the correct flag name.")
        return create_flag(flag_class=self._my_flags[flag_name][0],
                           flag_value_class=self._my_flags[flag_name][1],
                           flag_value=flag_value,
                           builder=builder)

    def get_all_flag_descriptions(self) -> list[str]:
        return [value[2] for key, value in self._my_flags.items()]
