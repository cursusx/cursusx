from abc import ABC
from collections.abc import Collection
from typing import Set, Mapping

from model.http.info.ContentModel import IterableContent

_SENTINEL = object()


class AbstractHeader(ABC):
    """
    This class represent a basic header implementation. The header class has a heder name
    and a header value like:
    header-name: <my_header_name>
    """
    _my_header_name: str
    _my_header_value: str

    def __init__(self, my_header_name: str = '', my_header_value: str = ''):
        if len(my_header_name) == 0 or len(my_header_value) == 0:
            raise TypeError(f"The header name cannot be None -> {my_header_name},"
                            f" the header value cannot be None -> {my_header_value}.")
        self._my_header_name = my_header_name
        self._my_header_value = my_header_value

    def get_header_name(self) -> str:
        """
        This http retuns the header name.
        :return: see above
        """
        return self._my_header_name

    def get_header_value(self) -> str:
        """
        This http retuns the header value.
        :return: see above
        """
        return self._my_header_value

    def __repr__(self) -> str:
        return f"""
        header-name: <{self._my_header_name}>
        header-value: <{self._my_header_value}>
        """

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AbstractHeader):
            return False

        other_object: AbstractHeader = other
        if other_object.get_header_name() != self._my_header_name:
            return False

        if other_object.get_header_value() != self._my_header_value:
            return False

        return True

    def __hash__(self) -> int:
        return hash((self._my_header_name, self._my_header_value))


class Header(AbstractHeader):
    """
    Basic header implementation.
    """

    def __init__(self, _sentinel: object = None, *, my_header_name: str, my_header_value: str):
        if _sentinel is not _SENTINEL:
            raise TypeError(
                "In order to create the Header you have to use the factory methods.")
        super().__init__(my_header_name, my_header_value)

    @classmethod
    def from_tuple(cls, value: tuple[str, str] = ('', '')) -> 'AbstractHeader':
        """
        Factory http for creating a Header object from a tuple of two strings.
        :param value: input tuple of two strings in the format HEADER-NAME: HEADER-VALUE
        :return: a new Header object
        """
        if not value or len(value) != 2:
            raise ValueError('The input value must not be empty and not None.')
        return cls(_sentinel=_SENTINEL, my_header_name=value[0], my_header_value=value[1])


class Headers(IterableContent[Mapping[str, str]]):
    """
    This class represents a collection of headers.
    """

    _my_headers: Set[AbstractHeader] = set()

    def __init__(self, _sentinel: object = None, *, headers: Collection[AbstractHeader]):
        if _sentinel is not _SENTINEL:
            raise TypeError(
                "In order to create the Headers class you have to use the factory methods.")

        for header in headers:
            self._my_headers.add(header)

    def get_headers(self) -> Set[AbstractHeader]:
        return self._my_headers

    def dump(self) -> Mapping[str, str]:
        return {header.get_header_name(): header.get_header_value() for header in self._my_headers}

    @classmethod
    def from_list(cls, headers: Collection[AbstractHeader]) -> 'Headers':
        """
        Factory http for creating a Headers object from a list of header. This factory http avoid to collect None headers.
        :param headers: input collection of headers
        :return: a new Headers object
        """
        if len(headers) == 0:
            raise ValueError('The input collection must not be empty.')
        return cls(_sentinel=_SENTINEL, headers=[header for header in headers if header])

    @classmethod
    def from_dictionary(cls, headers: Mapping[str, str]) -> 'Headers':
        return cls(_sentinel=_SENTINEL, headers=[Header.from_tuple((key, value)) for key, value in headers.items()])
