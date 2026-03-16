from abc import ABC, abstractmethod


class AbstractHost(ABC):
    _my_endpoint: str
    _my_port: int
