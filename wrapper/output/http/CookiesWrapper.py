from model.http.info.cookie.CookieModel import Cookies
from view.item.DictionaryViewerItem import DictionaryViewerItem


class CookiesWrapper(DictionaryViewerItem):
    DEFAULT_CSS = """
        CookiesWrapper {
            margin: 1 0;
            border: none;
        }

        CookiesWrapper ScrollableContainer {
            border: round #30363d;
            background: #161b22;
            padding: 1 2;
            height: 16;
            scrollbar-color: #30363d;
            scrollbar-background: #0d1117;
            scrollbar-size-vertical: 1;
        }
        """

    def __init__(self, cookies: Cookies = Cookies.empty(), title: str = "Cookies", **kwargs):
        super().__init__(values=cookies.dump(), title=title, **kwargs)
