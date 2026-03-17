import pytest

from model.http.info.BodyModel import AbstractBody, Body


def test_should_be_possible_to_create_empty_body():
    body: AbstractBody = Body.from_string()
    assert len(body.get_content()) == 0


def test_body_should_be_possible_to_retrieve_it():
    body: AbstractBody = Body.from_string('Random Body')
    assert body.get_content() is not None
    assert body.get_content() == 'Random Body'


def test_should_be_possible_to_create_body_from_empty_dict():
    body: AbstractBody = Body.from_dict({})
    assert body.get_content() is not None
    assert body.get_content() == ''
