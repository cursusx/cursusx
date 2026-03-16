from typing import NoReturn
import pytest

from model.message.HeaderMessage import HeaderMessage

def test_should_raise_value_error_when_value_is_empty() -> NoReturn:
    with pytest.raises(ValueError):
        HeaderMessage.from_tuple(None)


