from http import HTTPStatus

from view.item.LabelItem import LabelItem


class StatusCodeWrapper(LabelItem):
    DEFAULT_CSS = """
    StatusCodeWrapper {
        height: auto;
        margin: 1 0;
        padding: 1 2;
        border: round #3d4450;
        border-title-align: left;
        background: #0d1117;
    }

    StatusCodeWrapper .label {
        color: #6e7681;
        text-style: bold;
    }

    StatusCodeWrapper .value {
        color: #e6edf3;
        text-style: bold;
    }

    StatusCodeWrapper.success {
        border: round #3fb950;
        background: #0d1f14;
    }

    StatusCodeWrapper.success .label {
        color: #3fb950;
        text-style: bold italic;
    }

    StatusCodeWrapper.success .value {
        color: #3fb950;
        text-style: bold;
    }

    StatusCodeWrapper.error {
        border: round #f85149;
        background: #1f0d0d;
    }

    StatusCodeWrapper.error .label {
        color: #f85149;
        text-style: bold italic;
    }

    StatusCodeWrapper.error .value {
        color: #f85149;
        text-style: bold;
    }
    """

    def __init__(self, value: HTTPStatus, **kwargs):
        super().__init__(label="Status Code",
                         value=f"Code:{value.value} → {value.name}", **kwargs)
        self.remove_class("success", "error")
        self.add_class("success" if value.value < 400 else "error")
