import pytest

from model.http.info.parameter.ParameterModel import Parameter, AbstractParameter


def test_should_raise_type_error_when_value_is_empty() -> None:
    with pytest.raises(TypeError):
        Parameter.from_key_value('akey', '')


def test_should_raise_type_error_when_key_is_empty() -> None:
    with pytest.raises(TypeError):
        Parameter.from_key_value('', 'avalue')


def test_should_be_possible_to_create_parameter_from_tuple() -> None:
    parameter = Parameter.from_tuple(('key', 'value'))
    assert parameter.get_key() == 'key'
    assert parameter.get_value() == 'value'


def test_should_not_be_possible_to_use_parameter_constructor() -> None:
    with pytest.raises(TypeError):
        Parameter(None, key='a name', value='a value')


def test_should_be_possible_to_create_parameter_from_non_empty_values() -> None:
    try:
        Parameter.from_key_value('key', 'value')
    except ValueError:
        pytest.fail('When the input is not None it should be ok.')


def test_should_be_possible_to_retrieve_all_parameter_attributes() -> None:
    current: AbstractParameter = Parameter.from_key_value('key', 'value')
    assert current.get_key() == 'key'
    assert current.get_value() == 'value'
