from abc import ABC
from http import HTTPStatus

from model.message.HeaderModel import Headers


class AbstractResponseMessage(ABC):
    my_status_code: HTTPStatus
    my_headers: Headers
