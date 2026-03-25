
from model.http.info.header.HeaderModel import Headers
from view.item.DictionaryViewerItem import DictionaryViewerItem


class HeadersWrapper(DictionaryViewerItem):
    DEFAULT_CSS = """
    HeadersWrapper {
        margin: 1 0;
        border: none;
    }

    HeadersWrapper ScrollableContainer {
        border: round #30363d;
        background: #161b22;
        padding: 1 2;
        height: 16;
        scrollbar-color: #30363d;
        scrollbar-background: #0d1117;
        scrollbar-size-vertical: 1;
    }
    """

    def __init__(self, values: Headers = Headers.empty(), title: str = 'Headers', **kwargs) -> None:
        super().__init__(values.dump(), title, **kwargs)
