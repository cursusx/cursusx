from abc import ABC


class AbstractBody(ABC):
    _my_content: str

    def __init__(self, my_content: str=''):
        self._my_content = my_content