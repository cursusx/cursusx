from collections.abc import Mapping

from view.item.DictionaryViewerItem import DictionaryViewerItem


class HeadersWrapper(DictionaryViewerItem):
    def __init__(self, values: Mapping[str, str], title: str = 'Headers', **kwargs) -> None:
        super().__init__(values, title, **kwargs)
