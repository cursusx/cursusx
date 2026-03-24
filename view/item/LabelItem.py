from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static


class LabelItem(Vertical, Static):

    _my_label: str
    _my_value: str

    def __init__(self, label: str, value: str, **kwargs):
        super().__init__(value, **kwargs)
        self._my_label = label
        self._my_value = value

    def compose(self) -> ComposeResult:
        yield Static(self._my_label, classes="label")
        yield Static(self._my_value, classes="value")
