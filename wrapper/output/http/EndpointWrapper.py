from view.item.LabelItem import LabelItem


class EndpointWrapper(LabelItem):
    DEFAULT_CSS = """
    EndpointWrapper {
        height: auto;
        margin: 1 0;
        border: round #58a6ff;
        border-title-align: left;
        padding: 1 2;
        background: #0d1624;
    }

    EndpointWrapper .label {
        color: #58a6ff;
        text-style: bold italic;
    }

    EndpointWrapper .value {
        color: #cdd9e5;
        text-style: underline;
    }
    """

    def __init__(self, value: str, **kwargs):
        super().__init__(label="Endpoint: ", value=value, **kwargs)
