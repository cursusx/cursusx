from typing import Set

import pytest


from model.http.info.ParameterModel import Parameters, Parameter, AbstractParameter


def test_should_have_duplicate_parameters() -> None:
    parameters: Parameters = Parameters.from_list([
        Parameter.from_key_value('a', 'b'),
        Parameter.from_key_value('c', 'd'),
        Parameter.from_key_value('a', 'b'),
    ])
    assert len(parameters.get_parameters()) == 2

    expected: Set[AbstractParameter] = {
        Parameter.from_key_value('a', 'b'),
        Parameter.from_key_value('c', 'd')
    }

    assert all(
        parameters in expected for parameters in parameters.get_parameters())
