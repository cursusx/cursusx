from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue
from model.http.info.data.DataModel import HttpDataBuilder


def get_all_http_method_flags(http_data_builder: HttpDataBuilder) -> set[AbstractFlag[HttpDataBuilder]]:
    return {
        HttpMethodFlag(HttpMethodFlagValue(http_data_builder))
    }
