from textual.app import App, ComposeResult
from textual.widgets import Footer


class CursusxViewApp(App):
    def compose(self) -> ComposeResult:
        yield Footer()
