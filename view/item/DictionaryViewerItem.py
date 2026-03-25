from collections.abc import Mapping

from textual.widgets import Collapsible

from view.item.CustomScrollableContainer import CustomScrollableContainer


class DictionaryViewerItem(Collapsible):

    def __init__(self, values: Mapping[str, str], title: str, **kwargs):
        super().__init__(
            CustomScrollableContainer(values),
            title=title,
            **kwargs
        )
