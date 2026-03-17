from http import HTTPStatus

from model.http.info.BodyModel import AbstractBody
from model.http.info.ContentModel import AbstractContent
from model.http.info.EndpointModel import AbstractEndpoint
from model.http.info.HeaderModel import Headers
from model.http.info.ParameterModel import Parameters

_SENTINEL = object()


class ResponseContent(AbstractContent):
    """
    This class represents a http Response.
    """

    def __init__(self, _sentinel: object = None, *, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> None:
        if _sentinel is _SENTINEL:
            raise TypeError(
                "In order to create a Response you have to use the factory http.")
        super().__init__(endpoint, status_code, headers, parameters, body)

    @classmethod
    def create_response(cls, endpoint: AbstractEndpoint, status_code: HTTPStatus, headers: Headers, parameters: Parameters, body: AbstractBody) -> 'ResponseContent':
        return cls(_sentinel=_SENTINEL,
                   endpoint=endpoint,
                   status_code=status_code,
                   headers=headers,
                   parameters=parameters,
                   body=body)
