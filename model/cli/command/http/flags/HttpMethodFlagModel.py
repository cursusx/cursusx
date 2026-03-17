from http import HTTPMethod

from model.cli.command.FlagModel import AbstractFlag


class HttpMethodFlag(AbstractFlag):

    def get_flag_descritpion(self) -> str:
        return "Allows to specify the http method, the supported methods are"
