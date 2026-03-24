from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical

from view.CommandWidget import CommandWidget
from wrapper.http.BodyWrapper import BodyWrapper
from wrapper.http.EndpointWrapper import EndpointWrapper
from wrapper.http.HeadersWrapper import HeadersWrapper
from wrapper.http.ParametersWrapper import ParametersWrapper


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
    _my_parameters: ParametersWrapper
    _my_body: BodyWrapper
    _my_endpoint: EndpointWrapper

    def __init__(self, headers: HeadersWrapper,
                 parameters: ParametersWrapper,
                 body: BodyWrapper,
                 endpoint: EndpointWrapper,
                 **kwargs):
        super().__init__(**kwargs)
        self._my_headers = headers
        self._my_parameters = parameters
        self._my_body = body
        self._my_endpoint = endpoint

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="left-panel"):
                yield self._my_endpoint
            with Vertical(classes="right-panel"):
                yield self._my_body
                yield self._my_headers
                yield self._my_parameters
