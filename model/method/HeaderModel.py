from abc import ABC
from dataclasses import dataclass, field
from typing import NamedTuple, List


class AbstractHeader(ABC):
    """
    This class represent a basic header implementation. The header class has a heder name
    and a header value like:
    header-name: <my_header_name>
    """
    _my_header_name: str
    _my_header_value: str

    def __init__(self, my_header_name: str='', my_header_value: str=''):
        if len(my_header_name) == 0 or len(my_header_value) == 0:
            raise TypeError(f"The header name cannot be None -> {my_header_name},"
                            f" the header value cannot be None -> {my_header_value}.")
        self._my_header_name = my_header_name
        self._my_header_value = my_header_value

    def get_header_name(self) -> str:
        """
        This method retuns the header name.
        :return: see above
        """
        return self._my_header_name

    def get_header_value(self) -> str:
        """
        This method retuns the header value.
        :return: see above
        """
        return self._my_header_value

    def __repr__(self) -> str:
        return f"""
        header-name: <{self._my_header_name}>
        header-value: <{self._my_header_value}>
        """

class Header(AbstractHeader):
    """
    Basic header implementation.
    """
    def __init__(self, my_header_name: str, my_header_value: str):
        super().__init__(my_header_name, my_header_value)

    @classmethod
    def from_tuple(cls, value: tuple[str, str] = ('', '')) -> 'AbstractHeader':
        """
        Factory method for creating a Header object from a tuple of two strings.
        :param value: input tuple of two strings in the format HEADER-NAME: HEADER-VALUE
        :return: a new Header object
        """
        if not value or len(value) != 2:
            raise ValueError('The input value must not be empty and not None.')
        return cls(value[0], value[1])

@dataclass(frozen=True)
class Headers(NamedTuple):
    """
    This class represents a collection of headers.
    """
    my_headers: List[AbstractHeader] = field(default_factory=list)

    @classmethod
    def from_list(cls, headers: list[AbstractHeader]) -> 'Headers':
        """
        Factory method for creating a Headers object from a list of header.
        :param headers: input collection of headers
        :return: a new Headers object
        """
        return cls(list(headers))
