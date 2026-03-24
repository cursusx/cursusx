from view.item.LabelItem import LabelItem


class StatusCodeWrapper(LabelItem):
    def __init__(self, value: str, **kwargs):
        super().__init__(label="Status Code", value=value, **kwargs)
