from abc import abstractmethod, ABC
from http.server import HTTPServer, BaseHTTPRequestHandler


class AbstractMockHandler(ABC, BaseHTTPRequestHandler):
    @abstractmethod
    def do_GET(self) -> None:
        pass

    @abstractmethod
    def do_POST(self) -> None:
        pass

    @abstractmethod
    def do_PUT(self) -> None:
        pass

    @abstractmethod
    def do_DELETE(self) -> None:
        pass


class BasicMockHandler(AbstractMockHandler):
    def do_DELETE(self) -> None:
        self.send_response(200)
        self.end_headers()

    def do_PUT(self) -> None:
        self.send_response(200)
        self.end_headers()

    def do_POST(self) -> None:
        self.send_response(200)
        self.end_headers()

    def do_GET(self) -> None:
        self.send_response(200)
        self.end_headers()


def create_mock_server(url: str, port: int, mock_handler: type[AbstractMockHandler]) -> HTTPServer:
    # type: ignore[arg-type]
    return HTTPServer(server_address=(url, port), RequestHandlerClass=mock_handler)
