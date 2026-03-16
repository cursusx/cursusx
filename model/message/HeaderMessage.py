from abc import ABC
from dataclasses import dataclass, field
from typing import NamedTuple, List


@dataclass(frozen=True)
class AbstractHeaderMessage(ABC):
    my_header_name: str
    my_header_value: str

@dataclass(frozen=True)
class Headers(NamedTuple):
    my_headers: List[AbstractHeaderMessage] = field(default_factory=list)
