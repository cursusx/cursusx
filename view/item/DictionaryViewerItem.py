from collections.abc import Mapping

from textual.containers import ScrollableContainer
from textual.widgets import Collapsible, Pretty


class DictionaryViewerItem(Collapsible):
    DEFAULT_CSS = """
    DictionaryViewerItem {
        margin: 1 2;
    }
    DictionaryViewerItem ScrollableContainer {
        border: round $primary;
        padding: 1 2;
        height: 80vh;
    }
    """

    def __init__(self, values: Mapping[str, str], title: str, **kwargs):
        super().__init__(
            ScrollableContainer(Pretty(values)),
            title=title,
            **kwargs
        )
