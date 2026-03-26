from abc import ABC
from collections.abc import Mapping

from model.http.info.IterableContentModel import IterableContent, _T

_SENTINEL = object()


class AbstractCookie(ABC):
    """
    This class represents the Http Response Cookie.
    """
    _my_cookie_name: str
    _my_cookie_value: str

    def __init__(self, cookie_name: str, cookie_value: str):
        self.my_cookie_name = cookie_name
        self.my_cookie_value = cookie_value

    def get_cookies_name(self) -> str:
        return self.my_cookie_name

    def get_cookies_value(self) -> str:
        return self.my_cookie_value


class Cookie(AbstractCookie):
    def __init__(self, _sentinel: object = None, *, cookie_name: str, cookie_value: str):
        if _sentinel is None:
            raise Exception(
                "In order to create the Cookie class you have to use the factory methods.")
        super().__init__(cookie_name, cookie_value)

    @classmethod
    def from_key_value(cls, name: str, value: str) -> 'Cookie':
        if name == "" or value == "":
            raise ValueError("One of the input cookie's parameter are empty.")
        return cls(_sentinel=_SENTINEL, cookie_name=name, cookie_value=value)


class Cookies(IterableContent[Mapping[str, str]]):
    _my_cookies: Mapping[str, str]

    def __init__(self, _sentinel: object = None, *, cookies: Mapping[str, str]):
        if _sentinel is None:
            raise Exception(
                "In order to create the Cookies class you have to use the factory methods.")
        self._my_cookies = cookies

    def dump(self) -> Mapping[str, str]:
        return self._my_cookies

    @classmethod
    def from_collection(cls, cookies: list[AbstractCookie]) -> 'Cookies':
        if not cookies or len(cookies) == 0:
            raise ValueError("No cookies were given.")
        return cls(_sentinel=_SENTINEL, cookies={cookie.get_cookies_name(): cookie.get_cookies_value() for cookie in cookies})
