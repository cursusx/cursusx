from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.data.DataModel import HttpDataBuilder


class HttpCookiesFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, flag_value: AbstractFlagValue[HttpDataBuilder]):
        super().__init__(flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows to specify all the cookies"
