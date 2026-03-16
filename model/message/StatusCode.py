from typing import NamedTuple

all_my_status_codes: dict[int, str] = dict()

class StatusCode(NamedTuple):
    my_status_code: int
    my_status_message: str

    @classmethod
    def from_status_code(cls, status_code: int) -> 'StatusCode':
        return None
