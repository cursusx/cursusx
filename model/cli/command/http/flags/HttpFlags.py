from model.cli.command.FlagModel import AbstractFlag
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue
from model.http.info.content.RequestModel import RequestContentBuilder
from model.cli.command.http.Contants import HTTP_FLAG_METHOD


def create_flag(flag_name: str, request_builder: RequestContentBuilder) -> AbstractFlag[RequestContentBuilder]:
    if flag_name == HTTP_FLAG_METHOD:
        return HttpMethodFlag(HttpMethodFlagValue(request_builder))
    raise ValueError(f'Invalid flag name: {flag_name}')
