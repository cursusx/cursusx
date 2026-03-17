from http import HTTPMethod, HTTPStatus

from model.http.info.body.BodyModel import Body
from model.http.info.content.RequestModel import RequestContent, RequestContentBuilder
from model.http.info.data.DataModel import AbstractHttpData, HttpData
from model.http.info.header.HeaderModel import Headers, Header
from model.http.info.parameter.ParameterModel import Parameters, Parameter


def test_should_be_possible_to_retrieve_data_attributes():
    method: HTTPMethod = HTTPMethod.GET
    request: RequestContent = (RequestContentBuilder()
                               .add_body(Body.from_string('random body'))
                               .add_headers(
        Headers.from_list([
            Header.from_tuple(('key', 'value'))
        ]))
        .add_parameters(Parameters.from_list([Parameter.from_key_value('key', 'value')]))
        .add_status_code(HTTPStatus.OK)
        .build()
    )
    data: AbstractHttpData = HttpData.create_data(method,
                                                  request)
    assert data.get_http_method() == method
    assert data.get_http_request() is not None
