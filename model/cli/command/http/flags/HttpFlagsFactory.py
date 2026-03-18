from model.cli.command.FlagFactory import AbstractFlagFactory
from model.cli.command.http.Contants import HTTP_FLAG_METHOD
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue


class HttpFlagFactory(AbstractFlagFactory):
    _my_flags = {
        HTTP_FLAG_METHOD: (HttpMethodFlag, HttpMethodFlagValue),
    }
