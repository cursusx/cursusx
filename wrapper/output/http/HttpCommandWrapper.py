from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Label

from model.cli.command.http.HttpOutputModel import HttpOutput
from view.CommandWidget import CommandWidget
from wrapper.output.http.BodyWrapper import BodyWrapper
from wrapper.output.http.CookiesWrapper import CookiesWrapper
from wrapper.output.http.EndpointWrapper import EndpointWrapper
from wrapper.output.http.HeadersWrapper import HeadersWrapper
from wrapper.output.http.StatusCodeWrapper import StatusCodeWrapper


class HttpCommandWrapper(CommandWidget):
    DEFAULT_CSS = """
    HttpCommandWrapper {
        height: auto;
        background: #0d1117;
    }

    .left-panel {
        width: 50%;
        padding: 0 1;
        border-right: solid #21262d;
        align: left top;
    }

    .right-panel {
        width: 50%;
        padding: 0 1;
        align: left top;
    }

    .right-panel Collapsible {
        margin: 1 0;
        padding: 0;
        background: #161b22;
        border: round #30363d;
        height: auto;
    }

    .right-panel CollapsibleTitle {
        color: #6e7681;
        text-style: italic;
        background: #0d1117;
        padding: 0 2;
        margin: 0;
    }

    .right-panel CollapsibleTitle:hover {
        color: #58a6ff;
        background: #161b22;
    }

    .right-panel CollapsibleContent {
        height: auto;
        max-height: 24;
        padding: 0;
        margin: 0;
        background: #161b22;
    }

    .right-panel ScrollableContainer {
        border: round #30363d;
        background: #161b22;
        padding: 1 2;
        height: 24;
        scrollbar-color: #30363d;
        scrollbar-size-vertical: 1;
    }
    .panel-label {
        color: #6e7681;
        text-style: bold;
        margin: 0 0 1 0;
        padding: 0 1;
        border-bottom: solid #21262d;
        width: 100%;
    }
    """

    _my_headers: HeadersWrapper
    _my_status_code: StatusCodeWrapper
    _my_body: BodyWrapper
    _my_endpoint: EndpointWrapper
    _my_cookies: CookiesWrapper

    def __init__(self, http_output: HttpOutput, **kwargs):
        super().__init__(**kwargs)
        self._my_headers = HeadersWrapper(
            http_output.get_output().get_headers())
        self._my_body = BodyWrapper(
            http_output.get_output().get_body().get_content())
        self._my_endpoint = EndpointWrapper(
            http_output.get_output().get_endpoint().dump())
        self._my_status_code = StatusCodeWrapper(
            http_output.get_output().get_status_code())
        self._my_cookies = CookiesWrapper(
            http_output.get_output().get_cookies())

    def compose(self) -> ComposeResult:
        with Header():
            yield Label(content="Http command")
        with Horizontal():
            with Vertical(classes="left-panel"):
                yield Label("OVERVIEW", classes="panel-label")
                yield self._my_endpoint
                yield self._my_status_code
            with Vertical(classes="right-panel"):
                yield Label("PAYLOAD", classes="panel-label")
                yield self._my_body
                yield self._my_headers
                yield self._my_cookies
