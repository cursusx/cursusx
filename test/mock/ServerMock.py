from http.server import HTTPServer, BaseHTTPRequestHandler


class BasicMockHandler(BaseHTTPRequestHandler):
    def do_DELETE(self) -> None:
        self.send_response(200)

    def do_PUT(self) -> None:
        self.send_response(200)

    def do_POST(self) -> None:
        self.send_response(200)

    def do_GET(self) -> None:
        self.send_response(200)
