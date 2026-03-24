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

    def __init__(self, my_query_builder: HttpDataBuilder,
                 flag_value: str):
        super().__init__(my_query_builder, flag_value.upper())
        self.my_query_builder = my_query_builder

    def match_value(self) -> None:
        # match a value from the input val
        if self._my_flag_value not in self._my_supported_values:
            raise ValueError(
                f"The input method {self._my_flag_value} is not supported. All the supported values are: {self._my_supported_values}.")
        self.my_query_builder.add_http_method(
            HTTPMethod(value=self._my_flag_value))


class HttpMethodFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_METHOD
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows to specify the http method. The current supported methods are:"
