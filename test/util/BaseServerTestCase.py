import unittest
from http.server import HTTPServer


class BaseServerTestCase(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.my_server: HTTPServer | None = None

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()
