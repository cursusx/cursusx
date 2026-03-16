from typing import NamedTuple

all_my_status_codes: dict[int, str] = dict()

class StatusCode(NamedTuple):
    my_status_code: int
    my_status_message: str

    def __new__(cls, message: str, status_code: int, *, _internal=False):
        if not _internal:
            raise TypeError('You cannot create a StatusCode object, instead use the factory.')
        cls.my_status_code = status_code
        cls.my_status_message = message

    @classmethod
    def from_status_code(cls, status_code: int) -> 'StatusCode':
        if all_my_status_codes.get(status_code):
            return cls(all_my_status_codes[status_code], status_code, _internal=True)
        raise ValueError(f"The following status code {status_code} is not supported or likely wrong.")
