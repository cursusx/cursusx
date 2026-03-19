from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_ENDPOINT
from model.http.info.data.DataModel import HttpDataBuilder


class HttpEndpointFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_ENDPOINT
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows top specify the http endpoint."
