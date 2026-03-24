
from model.http.info.parameter.ParameterModel import Parameters
from view.item.DictionaryViewerItem import DictionaryViewerItem


class ParametersWrapper(DictionaryViewerItem):
    DEFAULT_CSS = """
       ParametersWrapper {
           margin: 1 2;
       }
       ParametersWrapper ScrollableContainer {
           border: round $primary;
           padding: 1 2;
           height: 80vh;
       }
       """

    def __init__(self, values: Parameters = Parameters.empty(), title: str = "Parameters", **kwargs):
        super().__init__(values.dump(), title, **kwargs)
