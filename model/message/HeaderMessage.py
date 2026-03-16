from abc import ABC
from typing import NamedTuple


class AbstractHeaderMessage(ABC):
    my_header_name: str
    my_header_value: str

class Headers(NamedTuple):
    my_headers: list[AbstractHeaderMessage]

    def __new__(cls, my_headers: list[AbstractHeaderMessage], *, _internal: bool=False):
        if not _internal:
            raise TypeError('You can not use the default contructor, instead use the factory class method.')
        cls.my_headers = my_headers

    @classmethod
    def create_headers_from_collection(cls, headers: list[AbstractHeaderMessage]=None) -> 'Headers':
        if not headers:
            headers = list()
        return Headers(headers, _internal=True)
