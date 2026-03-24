from textual.widgets import Static


class LabelItem(Static):
    def __init__(self, value: str, **kwargs):
        super().__init__(value, **kwargs)
