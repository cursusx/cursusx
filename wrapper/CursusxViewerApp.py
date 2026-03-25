
from textual import events
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer

from view.CommandWidget import CommandWidget


class CursusxViewerApp(App):
    BINDINGS = [Binding("q", "quit", "Quit")]
    _my_command_widget: CommandWidget

    def __init__(self, command_app: CommandWidget, **kwargs):
        super().__init__(**kwargs)
        self._my_command_widget = command_app

    async def _on_key(self, event: events.Key) -> None:
        if event.key == "Q":
            self.exit()

    def compose(self) -> ComposeResult:
        yield self._my_command_widget
        yield Footer()
