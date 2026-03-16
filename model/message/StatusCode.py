from typing import NamedTuple

all_my_status_codes: dict[int, str] = dict()

class StatusCode(NamedTuple):
    my_status_code: int
    my_status_message: str

    @classmethod
    def from_status_code(cls, status_code: int) -> 'StatusCode':
        if all_my_status_codes.get(status_code):
            return cls(status_code, all_my_status_codes[status_code])
        raise ValueError(f"The following status code {status_code} is not supported or likely wrong.")
