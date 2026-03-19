from abc import ABC
from typing import Collection, Iterable, Set

from model.http.info.IterableContentModel import IterableContent

_SENTINEL = object()


class AbstractParameter(ABC):
    """
    This class represents an abstract representation of a parameter.
    A parameter is a tuple of two strings: a key and a value.
    """
    _my_key: str
    _my_value: str

    def __init__(self, key: str, value: str):
        self._my_key = key
        self._my_value = value

    def get_key(self) -> str:
        """
        Retrusn the parameter's key.
        :return: see above.
        """
        return self._my_key

    def get_value(self) -> str:
        """
        Retrun the parameter's value.
        :return: see above.
        """
        return self._my_value

    def __eq__(self, other) -> bool:
        if not isinstance(other, AbstractParameter):
            return False
        return self.get_key() == other.get_key() and self.get_value() == other.get_value()

    def __hash__(self) -> int:
        return hash((self.get_key(), self.get_value()))


class Parameter(AbstractParameter):
    """
    Actual implementation for a parameter.
    """

    def __init__(self, _sentinel: object = None, *, key: str, value: str):
        if _sentinel is None:
            raise TypeError(
                "In order to create this class, use the factory method.")
        super().__init__(key, value)

    @classmethod
    def from_tuple(cls, parameter: tuple[str, str]) -> 'Parameter':
        """
        Factory method that allows to create the Parameter class from a tuple.
        :param parameter: input parameters.
        :return: see above.
        """
        if len(parameter) != 2:
            raise TypeError("The input tuple has to have a size of two.")
        if parameter[0] is None or parameter[1] is None:
            raise TypeError("The input values has to be different from None.")
        return cls(_sentinel=_SENTINEL, key=parameter[0], value=parameter[1])

    @classmethod
    def from_key_value(cls, key: str = '', value: str = '') -> 'Parameter':
        """
        Factory class that allows to create the Parameter class from a key and a string.
        :param key: input parameter's key.
        :param value: input parameter's value.
        :return: a new Parameter object.
        """
        if key == '' or value == '':
            raise TypeError("The key and the value cannot be empty.")
        return cls(_sentinel=_SENTINEL, key=key, value=value)


class Parameters(IterableContent[Iterable[tuple[str, str]]]):
    """
    This class represents a collection of parameters.
    """
    _my_parameters: set[Parameter]

    def __init__(self, _sentinel: object = None, *, my_parameters: set[Parameter]):
        if _sentinel is None:
            raise TypeError(
                'In order to create this class, use the factory method.')
        self._my_parameters = my_parameters

    def get_parameters(self) -> Set[Parameter]:
        """
        This method returns the collection of all parameters.
        :return: see above.
        """
        return self._my_parameters

    def dump(self) -> Iterable[tuple[str, str]]:
        """
        This method returns all the parameters of the class.
        :return: see above
        """
        return [(parameter.get_key(), parameter.get_value()) for parameter in self._my_parameters]

    @classmethod
    def from_list(cls, parameters: Collection[Parameter]) -> 'Parameters':
        """
        Factory method that allows to create the Parameters class from a list of parameters.
        :param parameters: input collection of parameters
        :return: a new Parameters object.
        """
        return cls(_sentinel=_SENTINEL, my_parameters={param for param in parameters if param})

    @classmethod
    def empty(cls) -> 'Parameters':
        """
        Factory method that creates an empty parameters object.
        :return: see above.
        """
        return cls(_sentinel=_SENTINEL, my_parameters=set())

    @classmethod
    def from_tuples(cls, parameters: Collection[tuple[str, str]]) -> 'Parameters':
        """
        Factory method that allows to create the Parameters class from a list of tuples.
        :param parameters: input collection of parameters
        :return: see above.
        """
        return cls(_sentinel=_SENTINEL, my_parameters={Parameter.from_key_value(param[0], param[1]) for param in parameters})
