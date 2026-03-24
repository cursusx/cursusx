from model.cli.command.FlagModel import AbstractFlag, AbstractFlagValue
from model.http.info.data.DataModel import HttpDataBuilder
from model.http.info.parameter.ParameterModel import Parameters


class HttpParametersFlagValue(AbstractFlagValue[HttpDataBuilder]):
    def __init__(self, my_query_builder: HttpDataBuilder, flag_value: str):
        super().__init__(my_query_builder, flag_value)

    def match_value(self) -> None:
        self._my_query_builder.add_parameters(
            Parameters.from_json_string(self._my_flag_value))


class HttpParametersFlag(AbstractFlag[HttpDataBuilder]):
    def __init__(self, my_flag_value: AbstractFlagValue[HttpDataBuilder]):
        super().__init__(my_flag_value)

    def get_flag_descritpion(self) -> str:
        return "This flag allows to specify the query parameters."
