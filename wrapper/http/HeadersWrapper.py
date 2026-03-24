
from model.http.info.header.HeaderModel import Headers
from view.item.DictionaryViewerItem import DictionaryViewerItem


class HeadersWrapper(DictionaryViewerItem):
    DEFAULT_CSS = """
    HeadersWrapper {
        margin: 1 2;
    }
    HeadersWrapper ScrollableContainer {
        border: round $primary;
        padding: 1 2;
        height: 80vh;
    }
    """

    def __init__(self, values: Headers = Headers.empty(), title: str = 'Headers', **kwargs) -> None:
        super().__init__(values.dump(), title, **kwargs)
