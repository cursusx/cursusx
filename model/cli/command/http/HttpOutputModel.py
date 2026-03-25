from model.cli.command.OutputModel import AbstractOutput
from model.http.info.content.ResponseModel import ResponseContent


class HttpOutput(AbstractOutput[ResponseContent]):
    def __init__(self, output: ResponseContent):
        super().__init__(output)

    def wrap_output(self) -> str:
        res = self.get_output()
        status_code = res.get_status_code()

        # Building the string with a structured, boxed aesthetic
        output = "╭" + "─" * 60 + "╮\n"
        output += f"│ ⚡ HTTP RESPONSE: {status_code} ({status_code.name})\n"
        output += "├" + "─" * 60 + "┤\n"

        output += "│ 📋 HEADERS\n"
        output += f"│ {res.get_headers()}\n"
        output += "├" + "─" * 60 + "┤\n"

        output += "│ 📄 BODY\n"
        body_content = res.get_body().get_content()
        indented_body = "\n".join(
            [f"│ {line}" for line in body_content.splitlines()])
        output += f"{indented_body}\n"

        output += "╰" + "─" * 60 + "╯"
        return output
