from textual.containers import ScrollableContainer
from textual.widgets import Collapsible, Pretty


class StringViewerItem(Collapsible):
    DEFAULT_CSS = """
       StringViewerItem: {
           margin: 1 2;
       }
       StringViewerItem ScrollableContainer {
           border: round $primary;
           padding: 1 2;
           height: 80vh;
       }
       """

    def __init__(self, content: str, title: str, **kwargs):
        super().__init__(
            ScrollableContainer(Pretty(content)),
            title=title,
            **kwargs
        )
