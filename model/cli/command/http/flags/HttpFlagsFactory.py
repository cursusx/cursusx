from model.cli.command.FlagFactory import AbstractFlagFactory
from model.cli.command.http.Contants import HTTP_FLAG_METHOD, HTTP_FLAG_ENDPOINT, HTTP_FLAG_HEADERS, \
    HTTP_FLAG_PARAMETERS, HTTP_FLAG_COOKIES, HTTP_FLAG_HELP
from model.cli.command.http.flags.HttpCookiesFlagModel import HttpCookiesFlag, HttpCookiesFlagValue
from model.cli.command.http.flags.HttpEndpointFlagModel import HttpEndpointFlag, HttpEndpointFlagValue
from model.cli.command.http.flags.HttpHeadersFlagModel import HttpHeadersFlag, HttpHeadersFlagValue
from model.cli.command.http.flags.HttpHelpFlagModel import HttpHelpFlag, HttpHelpFlagValue
from model.cli.command.http.flags.HttpMethodFlagModel import HttpMethodFlag, HttpMethodFlagValue
from model.cli.command.http.flags.HttpParametersFlagModel import HttpParametersFlag, HttpParametersFlagValue


class HttpFlagFactory(AbstractFlagFactory):
    _my_flags = {
        HTTP_FLAG_METHOD: (HttpMethodFlag, HttpMethodFlagValue, f"-{HTTP_FLAG_HEADERS}\t this flag allows you to specify the http method."),
        HTTP_FLAG_ENDPOINT: (HttpEndpointFlag, HttpEndpointFlagValue, f"-{HTTP_FLAG_ENDPOINT}\t this flag allows you to specify the http endpoint."),
        HTTP_FLAG_HEADERS: (HttpHeadersFlag, HttpHeadersFlagValue, f"-{HTTP_FLAG_HEADERS}\t this flag allows you to specify the http headers."),
        HTTP_FLAG_PARAMETERS: (HttpParametersFlag, HttpParametersFlagValue, f"-{HTTP_FLAG_PARAMETERS}\t this flag allows you to specify the http parameters."),
        HTTP_FLAG_COOKIES: (HttpCookiesFlag, HttpCookiesFlagValue, f"-{HTTP_FLAG_COOKIES}\t this flag allows you to specify the http cookies."),
        HTTP_FLAG_HELP: (HttpHelpFlag, HttpHelpFlagValue,
                         f"-{HTTP_FLAG_HELP}\t this flag allows you to dump all the flag information.")
    }
