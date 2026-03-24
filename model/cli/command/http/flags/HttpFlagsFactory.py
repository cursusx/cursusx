from model.cli.command.FlagFactory import AbstractFlagFactory
from model.cli.command.http.Contants import HTTP_FLAG_METHOD, HTTP_FLAG_ENDPOINT, HTTP_FLAG_HEADERS, \
    HTTP_FLAG_PARAMETERS
from model.cli.command.http.flags.HttpEndpointFlagModel import HttpEndpointFlag, HttpEndpointFlagValue
from model.cli.command.http.flags.HttpHeadersFlagModel import HttpHeadersFlag, HttpHeadersFlagValue
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue
from model.cli.command.http.flags.HttpParametersFlagModel import HttpParametersFlag, HttpParametersFlagValue


class HttpFlagFactory(AbstractFlagFactory):
    _my_flags = {
        HTTP_FLAG_METHOD: (HttpMethodFlag, HttpMethodFlagValue),
        HTTP_FLAG_ENDPOINT: (HttpEndpointFlag, HttpEndpointFlagValue),
        HTTP_FLAG_HEADERS: (HttpHeadersFlag, HttpHeadersFlagValue),
        HTTP_FLAG_PARAMETERS: (HttpParametersFlag, HttpParametersFlagValue),
    }
