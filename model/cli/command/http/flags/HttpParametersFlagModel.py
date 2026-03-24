from model.cli.command.FlagModel import AbstractFlag
from model.http.info.data.DataModel import HttpDataBuilder


class HttpParametersFlag(AbstractFlag[HttpDataBuilder]):
    def get_flag_descritpion(self) -> str:
        return "This flag allows to specify the query parameters."
