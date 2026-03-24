import re
from re import Match, Pattern

from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_ENDPOINT
from model.http.info.data.DataModel import HttpDataBuilder
from model.http.info.endpoint.EndpointModel import BasicEndpoint

IPV4 = r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)'
IPV6 = r'(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'          # full form
# compressed (::1, etc.)
IPV6_COMPRESSED = r'(?:[0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}'
HOST = rf'(?:{IPV4}|{IPV6}|\[{IPV6_COMPRESSED}\]|localhost)'
PORT = r'(?:[1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])'


class HttpEndpointFlagValue(AbstractFlagValue[HttpDataBuilder]):
    # ip:port
    # http://ip:port

    _my_pattern: Pattern[str] = re.compile(
        rf'^(?:https?://)?({HOST}):({PORT})$')

    def match_value(self) -> None:
        matches: Match | None = self._my_pattern.match(self._my_flag_value)
        if matches is None:
            raise Exception(
                f"Invalid http endpoint value: {self._my_flag_value}, you should specify the ip and the port and the protocol.")
        self._my_query_builder.add_endpoint(
            BasicEndpoint.create_endpoint(url=matches.group(1), port=int(matches.group(2))))


class HttpEndpointFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_ENDPOINT
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows top specify the http endpoint."
