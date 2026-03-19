import threading
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


def start_mock_server(url: str, port: int, mock_handler: type[AbstractMockHandler] = BasicMockHandler) -> HTTPServer:
    server: HTTPServer = HTTPServer(server_address=(
        url, port), RequestHandlerClass=mock_handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server
