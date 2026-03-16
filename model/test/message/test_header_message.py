import pytest

from model.message.HeaderModel import Header

def test_should_raise_value_error_when_value_is_empty() -> None:
    with pytest.raises(ValueError):
        Header.from_tuple()


