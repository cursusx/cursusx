from typing import Mapping

from view.item.DictionaryViewerItem import DictionaryViewerItem


class ParametersWrapper(DictionaryViewerItem):
    def __init__(self, values: Mapping[str, str], title: str = "Parameters", **kwargs):
        super().__init__(values, title, **kwargs)
