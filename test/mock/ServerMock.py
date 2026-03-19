class AbstractServerMock:
    _my_url: str
    _my_port: int

    def __init__(self, url: str, port: int):
        self._my_url = url
        self._my_port = port
