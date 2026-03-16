from abc import ABC
from dataclasses import dataclass, field
from typing import NamedTuple, List


class AbstractHeader(ABC):
    _my_header_name: str
    _my_header_value: str

    def __init__(self, my_header_name: str='', my_header_value: str=''):
        if len(my_header_name) == 0 or len(my_header_value) == 0:
            raise TypeError(f"The header name cannot be None -> {my_header_name},"
                            f" the header value cannot be None -> {my_header_value}.")
        self._my_header_name = my_header_name
        self._my_header_value = my_header_value

    def get_header_name(self) -> str:
        return self._my_header_name

    def get_header_value(self) -> str:
        return self._my_header_value

class Header(AbstractHeader):
    def __init__(self, my_header_name: str, my_header_value: str):
        super().__init__(my_header_name, my_header_value)

    @classmethod
    def from_tuple(cls, value: tuple[str, str] = ('', '')) -> 'AbstractHeader':
        if not value or len(value) != 2:
            raise ValueError('The input value must not be empty and not None.')
        return cls(value[0], value[1])

@dataclass(frozen=True)
class Headers(NamedTuple):
    my_headers: List[AbstractHeader] = field(default_factory=list)
