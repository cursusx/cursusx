from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.cookie.CookieModel import Cookies
from model.http.info.data.DataModel import HttpDataBuilder


class HttpCookiesFlagValue(AbstractFlagValue[HttpDataBuilder]):
    def __init__(self, my_query_builder: HttpDataBuilder, flag_value: str):
        super().__init__(my_query_builder, flag_value)

    def match_value(self) -> None:
        self._my_query_builder.add_cookies(
            Cookies.from_string(self._my_flag_value))


class HttpCookiesFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, flag_value: AbstractFlagValue[HttpDataBuilder]):
        super().__init__(flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows to specify all the cookies"
