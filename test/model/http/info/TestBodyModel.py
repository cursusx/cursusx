import pytest

from model.http.info.BodyModel import AbstractBody, Body


def test_should_be_possible_to_create_empty_body():
    body: AbstractBody = Body.from_string()
    assert len(body.get_content()) == 0
