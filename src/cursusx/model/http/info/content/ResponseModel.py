from http import HTTPStatus

from cursusx.model.http.info.body.BodyModel import AbstractBody
from cursusx.model.http.info.content.ContentModel import AbstractContent
from cursusx.model.http.info.endpoint.EndpointModel import AbstractEndpoint
from cursusx.model.http.info.header.HeaderModel import Headers
from cursusx.model.http.info.parameter.ParameterModel import Parameters

_SENTINEL = object()


class ResponseContent(AbstractContent):
    """
    This class represents a http Response.
    """
    _my_status: HTTPStatus

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> None:
        if _sentinel is None:
            raise TypeError(
                "In order to create a Response you have to use the factory http.")
        super().__init__(endpoint, headers, parameters, body)
        self._my_status_code = status_code

    def get_status_code(self) -> HTTPStatus:
        return self._my_status_code

    @classmethod
    def create_response(cls, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> 'ResponseContent':
        return cls(_sentinel=_SENTINEL,
                   endpoint=endpoint,
                   status_code=status_code,
                   headers=headers,
                   parameters=parameters,
                   body=body)
