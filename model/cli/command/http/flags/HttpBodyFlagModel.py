from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.data.DataModel import HttpDataBuilder


class HttpBodyFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "This flag allows to specify the body to send"
