from http import HTTPStatus

from view.item.LabelItem import LabelItem


class StatusCodeWrapper(LabelItem):
    DEFAULT_CSS = """
               StatusCodeWrapper {
                   height: auto;
                   margin: 1 0;
                   border-title-align: left;
                   padding: 1 2;
               }

               StatusCodeWrapper .label {
                   text-style: bold; 
                   color: $text-muted;
               }

               StatusCodeWrapper .value {
                   color: $text;
               }

               StatusCodeWrapper.success {
                   border: round green;
               }

               StatusCodeWrapper.success .label {
                   color: green;
               }

               StatusCodeWrapper.error {
                   border: round red;
               }

               StatusCodeWrapper.error .label {
                   color: red;
               }
               """

    def __init__(self, value: HTTPStatus, **kwargs):
        super().__init__(label="Status Code",
                         value=f"Code:{value.value} → {value.name}", **kwargs)
        self.remove_class("success", "error")
        self.add_class("success" if value.value < 400 else "error")
