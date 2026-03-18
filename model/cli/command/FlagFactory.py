from model.builder.BuilderModel import AbstractBuilder
from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_METHOD
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlagValue, HttpMethodFlag


def _create_flag(flag_class: type[AbstractFlag],
                 flag_value: type[AbstractFlagValue],
                 flag_name: str,
                 builder: AbstractBuilder) -> AbstractFlag:
    return flag_class(my_name=flag_name, my_flag_value=flag_value(my_query_builder=builder))


class FlagFactory:
    _my_flags: dict[str, tuple[type[AbstractFlag], type[AbstractFlagValue]]] = {
        HTTP_FLAG_METHOD: (HttpMethodFlag, HttpMethodFlagValue),
    }

    def __init__(self):
        raise ValueError('You can not use this constructor.')

    @staticmethod
    def create_flag(flag_name: str, builder: AbstractBuilder) -> AbstractFlag:
        if flag_name not in FlagFactory._my_flags:
            raise KeyError(
                f"{flag_name} not exist, specify the correct flagf name.")
        return _create_flag(flag_class=FlagFactory._my_flags[flag_name][0],
                            flag_value=FlagFactory._my_flags[flag_name][1],
                            flag_name=flag_name,
                            builder=builder)
