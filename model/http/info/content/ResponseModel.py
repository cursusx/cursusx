from http import HTTPStatus

from model.http.info.body.BodyModel import AbstractBody
from model.http.info.content.ContentModel import AbstractContent
from model.http.info.cookie.CookieModel import Cookies
from model.http.info.endpoint.EndpointModel import AbstractEndpoint
from model.http.info.header.HeaderModel import Headers
from model.http.info.parameter.ParameterModel import Parameters

_SENTINEL = object()


class ResponseContent(AbstractContent):
    """
    This class represents http Response.
    """
    _my_status: HTTPStatus
    _my_cookies: Cookies

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, cookies: Cookies, body: AbstractBody) -> None:
        if _sentinel is None:
            raise TypeError(
                "In order to create a Response you have to use the factory http.")
        super().__init__(endpoint, headers, parameters, body)
        self._my_status_code = status_code
        self._my_cookies = cookies

    def get_status_code(self) -> HTTPStatus:
        return self._my_status_code

    def get_cookies(self) -> Cookies:
        return self._my_cookies

    @classmethod
    def create_response(cls, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, cookies: Cookies, body: AbstractBody) -> 'ResponseContent':
        return cls(_sentinel=_SENTINEL,
                   endpoint=endpoint,
                   status_code=status_code,
                   headers=headers,
                   parameters=parameters,
                   cookies=cookies,
                   body=body)
