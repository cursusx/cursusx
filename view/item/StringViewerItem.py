from textual.containers import ScrollableContainer
from textual.widgets import Collapsible

from view.item.CustomScrollableContainer import CustomScrollableContainer


class StringViewerItem(Collapsible):
    _my_scrollable_container: ScrollableContainer

    def __init__(self, content: str, title: str, **kwargs):
        super().__init__(
            CustomScrollableContainer(content),
            title=title,
            **kwargs
        )
