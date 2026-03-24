from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_ENDPOINT
from model.http.info.data.DataModel import HttpDataBuilder
from model.http.info.endpoint.EndpointModel import BasicEndpoint


class HttpEndpointFlagValue(AbstractFlagValue[HttpDataBuilder]):
    def match_value(self) -> None:
        values: list[str] = self._my_flag_value.split(':')
        self._my_query_builder.add_endpoint(
            BasicEndpoint.create_endpoint(url=':'.join(values[0:2]), port=int(values[2])))


class HttpEndpointFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_ENDPOINT
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows top specify the http endpoint."
