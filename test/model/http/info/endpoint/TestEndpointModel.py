import pytest

from model.http.info.endpoint.EndpointModel import BasicEndpoint, AbstractEndpoint, UPPER_PORT_LIMIT


def test_should_be_possible_to_create_endpoint_with_url_and_port():
    endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
        'localhost', 8080)
    assert endpoint.get_url() == 'localhost'
    assert endpoint.get_port() == 8080
    assert endpoint.dump() == "localhost:8080"


def test_should_not_be_possible_to_create_endpoint_with_emtpy_url():
    with pytest.raises(ValueError):
        endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(port=8080)


def test_should_not_be_possible_to_create_endpoint_with_negative_port():
    with pytest.raises(ValueError):
        endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
            url='localhost', port=-1)


def test_should_not_be_possible_to_create_endpoint_with_port_bigger_than_uppder_limit():
    with pytest.raises(ValueError):
        endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
            url='localhost', port=UPPER_PORT_LIMIT + 1)
