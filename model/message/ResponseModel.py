from abc import ABC
from http import HTTPStatus

from model.message.HeaderModel import Headers


class AbstractResponseMessage(ABC):
    _my_status_code: HTTPStatus
    _my_headers: Headers
