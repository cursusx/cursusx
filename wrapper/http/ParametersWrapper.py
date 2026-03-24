
from model.http.info.parameter.ParameterModel import Parameters
from view.item.DictionaryViewerItem import DictionaryViewerItem


class ParametersWrapper(DictionaryViewerItem):
    def __init__(self, values: Parameters = Parameters.empty(), title: str = "Parameters", **kwargs):
        super().__init__(values.dump(), title, **kwargs)
