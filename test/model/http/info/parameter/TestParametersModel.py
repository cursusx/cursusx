from typing import Set

import pytest

from model.http.info.parameter.ParameterModel import Parameters, Parameter, AbstractParameter


def test_should_have_duplicate_parameters() -> None:
    parameters: Parameters = Parameters.from_list([
        Parameter.from_key_value('a', 'b'),
        Parameter.from_key_value('c', 'd'),
        Parameter.from_key_value('a', 'b'),
    ])
    assert len(parameters.get_parameters_set()) == 2

    expected: Set[AbstractParameter] = {
        Parameter.from_key_value('a', 'b'),
        Parameter.from_key_value('c', 'd')
    }

    assert all(
        parameters in expected for parameters in parameters.get_parameters_set())


def test_should_raise_error_when_input_collection_is_empty() -> None:
    with pytest.raises(ValueError):
        params: Parameters = Parameters.from_list(parameters=[])
