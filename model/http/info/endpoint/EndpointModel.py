from abc import ABC

_SENTINEL = object()
UPPER_PORT_LIMIT = 65535


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

    def dump(self) -> str:
        return f"{self._my_url}:{self._my_port}"


class BasicEndpoint(AbstractEndpoint):

    def __init__(self, _sentinel: object = None, *,  url: str, port: int):
        if _sentinel is None:
            raise TypeError(
                "In order to create the endpoint you should use the factory method.")
        super().__init__(url, port)

    @classmethod
    def create_endpoint(cls, url: str = '', port: int = -1) -> 'BasicEndpoint':
        if url == '':
            raise ValueError("The url cannot be empty.")
        if port < 0 or port > UPPER_PORT_LIMIT:
            raise ValueError("Port must be between 0 and 65535.")
        return cls(_sentinel=_SENTINEL, url=url, port=port)
