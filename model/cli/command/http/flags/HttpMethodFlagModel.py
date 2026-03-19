import re
from http import HTTPMethod
from re import Pattern

from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_METHOD
from model.http.info.data.DataModel import HttpDataBuilder

# cursurx http -method=get


class HttpMethodFlagValue(AbstractFlagValue[HttpDataBuilder]):
    _my_query_builder: HttpDataBuilder
    _my_supported_values: set[str] = {
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.PUT,
        HTTPMethod.DELETE,
        HTTPMethod.PATCH
    }
    _my_representation: Pattern = re.compile(r"-method=*")  # TODO

    def __init__(self, my_query_builder: HttpDataBuilder,
                 flag_value: str):
        super().__init__(my_query_builder, flag_value)
        self.my_query_builder = my_query_builder

    def match_value(self) -> None:
        # match a value from the input val
        # TODO: match the value
        self.my_query_builder.add_http_method(HTTPMethod.GET)


class HttpMethodFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_METHOD
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows to specify the http method. The current supported methods are:"
