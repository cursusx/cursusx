from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.data.DataModel import HttpDataBuilder


class HttpHelpFlagValue(AbstractFlagValue[HttpDataBuilder]):
    def __init__(self, my_query_builder: HttpDataBuilder, flag_value: str):
        super().__init__(my_query_builder, flag_value)

    def match_value(self) -> None:
        return


class HttpHelpFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "This flag allows you to dump all the information regarding the current command."
