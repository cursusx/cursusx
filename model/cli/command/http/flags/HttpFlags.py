from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue
from model.http.info.content.RequestModel import RequestContentBuilder


def get_all_http_method_flags() -> set[AbstractFlag[RequestContentBuilder]]:
    request_builder = RequestContentBuilder()
    return {
        HttpMethodFlag(HttpMethodFlagValue(request_builder))
    }
