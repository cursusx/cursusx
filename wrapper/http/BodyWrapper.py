from view.item.StringViewerItem import StringViewerItem


class BodyWrapper(StringViewerItem):
    def __init__(self, content: str, title: str = "Body", **kwargs):
        super().__init__(content, title, **kwargs)
