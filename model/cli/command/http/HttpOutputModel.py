from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import TypeVar

from model.cli.command.OutputModel import AbstractOutput
from model.http.info.content.ResponseModel import ResponseContent

_T = TypeVar("_T")


class AbstractHttpOutput(AbstractOutput[_T]):

    @abstractmethod
    def wrap_output(self) -> str:
        pass


class HttpOutput(AbstractHttpOutput[ResponseContent]):
    def __init__(self, output: ResponseContent):
        super().__init__(output)

    def wrap_output(self) -> str:
        res: ResponseContent = self.get_output()
        status_code: HTTPStatus = res.get_status_code()

        output = "╭" + "─" * 60 + "╮\n"
        output += f"│ ⚡ HTTP RESPONSE: {status_code} ({status_code.name})\n"
        output += self._draw_line()

        output += "│ 📋 HEADERS\n"
        output += f"│ {res.get_headers()}\n"
        output += self._draw_line()

        output += "│ 📋 COOKIES\n"
        output += f"│ {res.get_cookies()}\n"
        output += self._draw_line()

        output += "│ 📄 BODY\n"
        body_content: str = res.get_body().get_content()
        indented_body = "\n".join(
            [f"│ {line}" for line in body_content.splitlines()])
        output += f"{indented_body}\n"

        output += "╰" + "─" * 60 + "╯"
        return output

    def _draw_line(self, length: int = 60) -> str:
        return "├" + "─" * length + "┤\n"


class HttpHelpOutput(AbstractHttpOutput[str]):
    def __init__(self, output: str):
        super().__init__(output)

    def wrap_output(self) -> str:
        return self.get_output()
