from abc import ABC


class AbstractHeaderMessage(ABC):
    my_header_name: str
    my_header_value: str

class Headers:
    my_headers: list[AbstractHeaderMessage]