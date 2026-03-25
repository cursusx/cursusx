from abc import ABC
from typing import Any

_SENTINEL = object()


class AbstractBody(ABC):
    """
    This class represents the http's body.
    """
    _my_content: str

    def __init__(self, my_content: str = ''):
        self._my_content = my_content

    def get_content(self) -> str:
        return self._my_content


class Body(AbstractBody):
    def __init__(self, _sentinel: object = None, *, content: str):
        if _sentinel is not _SENTINEL:
            raise ValueError(
                'In order to create the body use the factory http.')
        super().__init__(content)

    @classmethod
    def from_string(cls, content: str = '') -> 'Body':
        """
        This factory method creates a Body from the input content string.
        :param content: input content to store
        :return: a new Body object
        """
        return cls(_sentinel=_SENTINEL, content=content)

    @classmethod
    def empty(cls):
        return cls(_sentinel=_SENTINEL, content='')

    @classmethod
    def from_dict(cls, content: dict[Any, Any]) -> 'Body':
        """
        This factory method creates a Body from the input content dictionary.
        :param content: input content dict to store
        :return: a new Body object
        """
        import json
        if len(content) == 0:
            return cls(_sentinel=_SENTINEL, content='')
        return cls(_sentinel=_SENTINEL, content=json.dumps(content))
