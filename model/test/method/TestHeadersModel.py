from typing import Set

import pytest

from model.method.HeaderModel import Headers, Header, AbstractHeader


def test_should_have_duplicate_headers() -> None:
    headers: Headers = Headers.from_list([
        Header.from_tuple(('a', 'b')),
        Header.from_tuple(('a', 'b')),
        Header.from_tuple(('c', 'd'))
    ])
    assert len(headers.get_headers()) == 2

    expected: Set[AbstractHeader] = {
        Header.from_tuple(('a', 'b')),
        Header.from_tuple(('c', 'd'))
    }

    assert all(header in expected for header in headers.get_headers())
