from view.item.StringViewerItem import StringViewerItem
import json


class BodyWrapper(StringViewerItem):
    DEFAULT_CSS = """
    BodyWrapper {
        margin: 1 0;
    }

    BodyWrapper ScrollableContainer {
        border: round #30363d;
        background: #161b22;
        padding: 1 2;
        height: 16;
        scrollbar-color: #30363d;
        scrollbar-background: #0d1117;
        scrollbar-size-vertical: 1;
    }
    """

    def __init__(self, content: str, title: str = "Body", **kwargs):
        try:
            super().__init__(json.loads(content), title, **kwargs)
        except json.decoder.JSONDecodeError:
            super().__init__(content, title, **kwargs)
