from abc import ABC, abstractmethod


class AbstractEndpoint(ABC):
    _my_url: str
    _my_port: int

    def __init__(self, url: str, port: int):
        self._my_url = url
        self._my_port = port

    def get_url(self) -> str:
        return self._my_url

    def get_port(self) -> int:
        return self._my_port

class BasicEndpoint(AbstractEndpoint):

    def __init__(self, url: str, port: int):
        super().__init__(url, port)
    #TODO: add factory method, add tests