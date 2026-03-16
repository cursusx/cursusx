from abc import ABC
from dataclasses import dataclass, field
from typing import NamedTuple, List


class AbstractHeader(ABC):
    my_header_name: str
    my_header_value: str

    def __init__(self, my_header_name: str=None, my_header_value: str=None):
        if not my_header_name or not my_header_value:
            raise TypeError(f"The header name cannot be None -> {my_header_name},"
                            f" the header value cannot be None -> {my_header_value}.")
        self.my_header_name = my_header_name
        self.my_header_value = my_header_value

@dataclass(frozen=True)
class Header(AbstractHeader):
    def __init__(self, my_header_name: str, my_header_value: str):
        super().__init__(my_header_name, my_header_value)
    @classmethod
    def from_tuple(cls, value: tuple[str, str]=None) -> 'AbstractHeader':
        if not value:
            raise ValueError('The input value must not be empty and not None.')
        return cls(value[0], value[1])

@dataclass(frozen=True)
class Headers(NamedTuple):
    my_headers: List[AbstractHeader] = field(default_factory=list)
