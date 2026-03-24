from textual.app import App, ComposeResult

from view.CommandWidget import CommandWidget


class CursusxViewerApp(App):
    _my_command_widget: CommandWidget

    def __init__(self, command_app: CommandWidget, **kwargs):
        super().__init__(**kwargs)
        self._my_command_widget = command_app

    def compose(self) -> ComposeResult:
        yield self._my_command_widget
