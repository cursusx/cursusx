from view.item.LabelItem import LabelItem


class StatusCodeWrapper(LabelItem):
    DEFAULT_CSS = """
           StatusCodeWrapper {
               height: auto;
               margin: 1 0;
               border: round $primary;
               border-title-align: left;
               padding: 1 2;
           }

           StatusCodeWrapper .label {
               color: $text-muted;
           }

           StatusCodeWrapper .value {
               color: $text;
           }
           
           StatusCodeWrapper .success {
               color: round green;
           }
           
           StatusCodeWrapper .error{
               color: round red;
           }
           """

    def __init__(self, value: str, **kwargs):
        super().__init__(label="Status Code", value=value, **kwargs)
        self.remove_class("success", "error")
        self.add_class("success" if int(value) < 400 else "error")
