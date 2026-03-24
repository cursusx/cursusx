
from model.http.info.header.HeaderModel import Headers
from view.item.DictionaryViewerItem import DictionaryViewerItem


class HeadersWrapper(DictionaryViewerItem):
    def __init__(self, values: Headers = Headers.empty(), title: str = 'Headers', **kwargs) -> None:
        super().__init__(values.dump(), title, **kwargs)
