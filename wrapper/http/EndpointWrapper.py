from view.item.LabelItem import LabelItem


class EndpointWrapper(LabelItem):
    def __init__(self, value: str, **kwargs):
        super().__init__(value, **kwargs)
