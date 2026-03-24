from view.item.StringViewerItem import StringViewerItem


class BodyWrapper(StringViewerItem):
    DEFAULT_CSS = """
       BodyWrapper {
           margin: 1 2;
       }
       BodyWrapper ScrollableContainer {
           border: round $primary;
           padding: 1 2;
           height: 80vh;
       }
       """

    def __init__(self, content: str, title: str = "Body", **kwargs):
        super().__init__(content, title, **kwargs)
