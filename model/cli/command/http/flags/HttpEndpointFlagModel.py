from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.cli.command.http.Contants import HTTP_FLAG_ENDPOINT
from model.http.info.data.DataModel import HttpDataBuilder
from model.http.info.endpoint.EndpointModel import BasicEndpoint


class HttpEndpointFlagValue(AbstractFlagValue[HttpDataBuilder]):
    def match_value(self) -> None:
        self._my_query_builder.add_endpoint(
            BasicEndpoint.create_endpoint(url='http://localhost', port=8080))


class HttpEndpointFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        self._my_name = HTTP_FLAG_ENDPOINT
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "Allows top specify the http endpoint."
