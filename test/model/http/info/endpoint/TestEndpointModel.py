from model.http.info.endpoint.EndpointModel import BasicEndpoint, AbstractEndpoint


def test_should_be_possible_to_create_endpoint_with_url_and_port():
    endpoint: AbstractEndpoint = BasicEndpoint.create_endpoint(
        'localhost', 8080)
    assert endpoint.get_url() == 'localhost'
    assert endpoint.get_port() == 8080
    assert endpoint.dump() == "localhost:8080"
