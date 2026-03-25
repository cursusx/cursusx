from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Label

from cursusx.model.cli.command.http.HttpOutputModel import HttpOutput
from view.CommandWidget import CommandWidget
from wrapper.http.BodyWrapper import BodyWrapper
from wrapper.http.EndpointWrapper import EndpointWrapper
from wrapper.http.HeadersWrapper import HeadersWrapper
from wrapper.http.StatusCodeWrapper import StatusCodeWrapper


class HttpCommandWrapper(CommandWidget):
    DEFAULT_CSS = """
     HttpCommandWidget {
         height: auto;
     }
     
     .left-panel {
         width: 50%;
         padding: 1;
     }

     .right-panel {
         width: 50%;
         padding: 1;
     }

     .right-panel ScrollableContainer {
         height: 20;
         border: round $primary;
         padding: 1;
     }

     .right-panel Collapsible {
         margin-bottom: 1;
     }
     """

    _my_headers: HeadersWrapper
    _my_status_code: StatusCodeWrapper
    _my_body: BodyWrapper
    _my_endpoint: EndpointWrapper

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

    def compose(self) -> ComposeResult:
        with Header():
            yield Label(content="Http command")
        with Horizontal():
            with Vertical(classes="left-panel"):
                yield self._my_endpoint
                yield self._my_status_code
            with Vertical(classes="right-panel"):
                yield self._my_body
                yield self._my_headers
