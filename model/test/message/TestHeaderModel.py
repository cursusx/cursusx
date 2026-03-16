import pytest

from model.message.HeaderModel import Header, AbstractHeader


def test_should_raise_value_error_when_value_is_empty() -> None:
    with pytest.raises(TypeError):
        Header.from_tuple()

def test_should_be_possible_to_create_header_from_non_empty_tuple() -> None:
    try:
        Header.from_tuple(('content-type', 'text/html'))
    except ValueError:
        pytest.fail('When the input is a tuple it should be ok.')

def test_should_be_possible_to_retrieve_all_header_attributes() -> None:
    current: AbstractHeader = Header.from_tuple(('content-type', 'text/html'))
    assert current.get_header_name() == 'content-type'
    assert current.get_header_value() == 'text/html'

def test_should_represent_the_correct_value() -> None:
    current: AbstractHeader = Header.from_tuple(('content-type', 'text/html'))
    assert current.__repr__().replace(' ', '').strip() == """
    header-name: <content-type>
    header-value: <text/html>
    """.strip().replace(' ', '')
