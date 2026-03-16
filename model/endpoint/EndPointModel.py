from abc import ABC


class AbstractEndpoint(ABC):
    my_endpoint: str

    def __init__(self, my_endpoint: str):
        if self.__validate_endpoint(my_endpoint):
            self.my_endpoint = my_endpoint

    def __validate_endpoint(self, endpoint: str) -> bool:
        if endpoint:
            return False
        return True
