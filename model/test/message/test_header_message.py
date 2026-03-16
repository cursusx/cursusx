import pytest

from model.message.HeaderModel import Header

def test_should_raise_value_error_when_value_is_empty() -> None:
    with pytest.raises(TypeError):
        Header.from_tuple()

def test_should_be_possible_to_create_header_from_non_empty_tuple() -> None:
    try:
        Header.from_tuple(('content-type', 'text/html'))
    except ValueError:
        pytest.fail('When the input is a tuple it should be ok.')


