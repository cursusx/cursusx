from abc import ABC
from dataclasses import dataclass, field
from typing import NamedTuple, List


@dataclass(frozen=True)
class AbstractHeaderMessage(ABC):
    my_header_name: str
    my_header_value: str

    @classmethod
    def from_tuple(cls, value: tuple[str, str]=None) -> 'AbstractHeaderMessage':
        if not value:
            raise ValueError('The input value must not be empty and not None.')
        return cls(value[0], value[1])



@dataclass(frozen=True)
class Headers(NamedTuple):
    my_headers: List[AbstractHeaderMessage] = field(default_factory=list)
