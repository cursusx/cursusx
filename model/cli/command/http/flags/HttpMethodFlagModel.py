import re
from http import HTTPMethod
from re import Pattern

from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.content.RequestModel import RequestContentBuilder

# cursurx http -method=get


class HttpMethodFlagValue(AbstractFlagValue[RequestContentBuilder]):
    _my_query_builder: RequestContentBuilder
    _my_supported_values: set[str] = {
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.PUT,
        HTTPMethod.DELETE,
        HTTPMethod.PATCH
    }
    _my_representation: Pattern = re.compile(r"-method=*")

    def __init__(self, my_query_builder: RequestContentBuilder):
        super().__init__(my_query_builder)

    def match_value(self, flag_value: str) -> None:
        return


class HttpMethodFlag(AbstractFlag[RequestContentBuilder]):
    def __init__(self, name: str, value: AbstractFlagValue[RequestContentBuilder]):
        super().__init__(name, value)

    def get_flag_descritpion(self) -> str:
        return "Allows to specify the http method. The current supported methods are:"
