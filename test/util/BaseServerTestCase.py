import unittest
from http.server import HTTPServer

from test.mock.ServerMock import start_mock_server, kill_mock_server


class BaseServerTestCase(unittest.TestCase):
    __test__ = False
    _url: str
    _port: int
    my_server: HTTPServer

    def __init__(self, url: str, port: int, method_name: str = "runTest"):
        super().__init__(method_name)
        self.url = url
        self._port = port

    def setUp(self) -> None:
        super().setUp()
        self.my_server: HTTPServer = start_mock_server(
            self.url, self._port)

    def tearDown(self) -> None:
        super().tearDown()
        kill_mock_server(self.my_server)
