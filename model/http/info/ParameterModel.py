from abc import ABC
from typing import Collection, Iterable

from model.http.info.BodyModel import AbstractBody
from model.http.info.ContentModel import IterableContent

_SENTINEL = object()


class AbstractParameter(ABC):
    _my_key: str
    _my_value: str

    def __init__(self, key: str, value: str):
        self._my_key = key
        self._my_value = value

    def get_key(self) -> str:
        return self._my_key

    def get_value(self) -> str:
        return self._my_value

    def __eq__(self, other) -> bool:
        if not isinstance(other, AbstractParameter):
            return False
        return self.get_key() == other.get_key() and self.get_value() == other.get_value()

    def __hash__(self) -> int:
        return hash((self.get_key(), self.get_value()))


class Parameter(AbstractParameter):
    def __init__(self, _sentinel: object = None, *, key: str, value: str):
        if _sentinel is None:
            raise TypeError(
                "In order to create this class, use the factory method.")
        super().__init__(key, value)

    @classmethod
    def from_key_value(cls, key: str = '', value: str = '') -> 'Parameter':
        if key == '' or value == '':
            raise TypeError("The key and the value cannot be empty.")
        return cls(_sentinel=_SENTINEL, key=key, value=value)


class Parameters(IterableContent[Iterable[tuple[str, str]]]):
    _my_parameters: set[Parameter]

    def __init__(self, _sentinel: object = None, *, my_parameters: set[Parameter]):
        if _sentinel is None:
            raise TypeError(
                'In order to create this class, use the factory method.')
        self._my_parameters = my_parameters

    def dump(self) -> Iterable[tuple[str, str]]:
        """
        This method returns all the parameters of the class.
        :return: see above
        """
        return [(parameter.get_key(), parameter.get_value()) for parameter in self._my_parameters]

    @classmethod
    def from_list(cls, parameters: Collection[Parameter]) -> 'Parameters':
        return cls(_sentinel=_SENTINEL, my_parameters={param for param in parameters})

    @classmethod
    def from_tuples(cls, parameters: Collection[tuple[str, str]]) -> 'Parameters':
        return cls(_sentinel=_SENTINEL, my_parameters={Parameter.from_key_value(param[0], param[1]) for param in parameters})
