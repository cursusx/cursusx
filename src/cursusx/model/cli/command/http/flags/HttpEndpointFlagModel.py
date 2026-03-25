import re
from re import Match, Pattern

from cursusx.model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from cursusx.model.cli.command.http.Contants import HTTP_FLAG_ENDPOINT
from cursusx.model.http.info.data.DataModel import HttpDataBuilder
from cursusx.model.http.info.endpoint.EndpointModel import BasicEndpoint

IPV4 = r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)'
IPV6 = r'(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
IPV6_COMPRESSED = r'(?:[0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}'
HOST = rf'(?:{IPV4}|{IPV6}|\[{IPV6_COMPRESSED}\]|localhost)'
PORT = r'(?:[1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])'


class HttpEndpointFlagValue(AbstractFlagValue[HttpDataBuilder]):
    # ip:port
    # http://ip:port

    _my_pattern_with_protocol: Pattern[str] = re.compile(
        rf'^(https?://)({HOST}):({PORT})$')

    _my_pattern_without_protocol: Pattern[str] = re.compile(
        rf'^(?:https?://)?({HOST}):({PORT})$')

    def match_value(self) -> None:
        matches: Match | None = self._my_pattern_with_protocol.match(
            self._my_flag_value)
        if matches:
            self._my_query_builder.add_endpoint(
                BasicEndpoint.create_endpoint(url=f"{matches.group(1)}{matches.group(2)}", port=int(matches.group(3))))
        else:
            matches: Match | None = self._my_pattern_without_protocol.match(
                self._my_flag_value)
            if matches:
                self._my_query_builder.add_endpoint(
                    BasicEndpoint.create_endpoint(url=matches.group(1),
                                                  port=int(matches.group(2))))
            else:
                raise Exception(
                    f"Invalid http endpoint value: {self._my_flag_value}, you should specify the ip and the port and the protocol.")


class HttpEndpointFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_ENDPOINT
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows top specify the http endpoint."
