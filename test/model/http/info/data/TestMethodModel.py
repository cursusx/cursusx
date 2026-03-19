from http import HTTPMethod, HTTPStatus

from model.http.info.body.BodyModel import Body
from model.http.info.content.RequestModel import RequestContent, RequestContentBuilder
from model.http.info.data.DataModel import AbstractHttpData, HttpData
from model.http.info.endpoint.EndpointModel import BasicEndpoint
from model.http.info.header.HeaderModel import Headers, Header, AbstractHeader
from model.http.info.parameter.ParameterModel import Parameters, Parameter, AbstractParameter


def test_should_be_possible_to_retrieve_data_attributes():
    method: HTTPMethod = HTTPMethod.GET
    request: RequestContent = (RequestContentBuilder()
                               .add_body(Body.from_string('random body'))
                               .add_headers(
        Headers.from_list([
            Header.from_tuple(('key', 'value'))
        ]))
        .add_parameters(Parameters.from_list([Parameter.from_key_value('key', 'value')]))
        .add_endpoint(BasicEndpoint.create_endpoint('localhost', 80))
        .build()
    )
    data: AbstractHttpData = HttpData.create_data(method,
                                                  request)
    expected_parameters: set[AbstractParameter] = {
        Parameter.from_key_value('key', 'value')}
    expected_headers: set[AbstractHeader] = {
        Header.from_tuple(('key', 'value'))}
    assert data.get_http_method() == method
    assert data.get_http_request() is not None
    assert all(param in expected_parameters for param in data.get_http_request(
    ).get_parameters().get_parameters_set())
    assert all(header in expected_headers for header in data.get_http_request(
    ).get_headers().get_headers_set())
    assert data.get_http_request().get_status_code() == HTTPStatus.OK
    assert data.get_http_request().get_endpoint().dump() == "localhost:80"
