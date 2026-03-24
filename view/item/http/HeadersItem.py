from textual.widgets import Collapsible


class HeadersItem(Collapsible):
    DEFAULT_CSS = """
    HeadersItem: {
        margin: 1 2;
    }
    HeadersItem ScrollableContainer {
        border: round $primary;
        padding: 1 2;
        height: 80vh;
    }
    """
