from typing import TypeVar, Generic

from textual.binding import Binding
from textual.containers import ScrollableContainer
from textual.widgets import Pretty

T = TypeVar("T")


class CustomScrollableContainer(ScrollableContainer, Generic[T]):
    BINDINGS = [Binding("w", "up", "Scroll Up"),
                Binding("s", "down", "Scroll Down")]

    def __init__(self, content: T):
        super().__init__(Pretty(content))

    def action_down(self):
        self.scroll_down()

    def action_up(self):
        self.scroll_up()
