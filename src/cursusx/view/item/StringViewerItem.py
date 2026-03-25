from textual.containers import ScrollableContainer
from textual.widgets import Collapsible, Pretty


class StringViewerItem(Collapsible):
    def __init__(self, content: str, title: str, **kwargs):
        super().__init__(
            ScrollableContainer(Pretty(content)),
            title=title,
            **kwargs
        )
