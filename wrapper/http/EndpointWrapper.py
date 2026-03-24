from view.item.LabelItem import LabelItem


class EndpointWrapper(LabelItem):
    DEFAULT_CSS = """
       EndpointWrapper {
           height: auto;
           margin: 1 0;
           border: round $primary;
           border-title-align: left;
           padding: 1 2;
       }

       EndpointWrapper .label {
           color: $text-muted;
       }

       EndpointWrapper .value {
           color: $text;
       }
       """

    def __init__(self, value: str, **kwargs):
        super().__init__(label="Endpoint: ", value=value, **kwargs)
