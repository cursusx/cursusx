from model.cli.command.OutputModel import AbstractOutput
from model.cli.command.http.HttpOutputModel import HttpOutput
from view.CommandWidget import CommandWidget
from wrapper.output.http.HttpCommandWrapper import HttpCommandWrapper


def get_viewer_command_widget[T](output: AbstractOutput[T]) -> CommandWidget:
    if isinstance(output, HttpOutput):
        return HttpCommandWrapper(output)
    raise NotImplementedError("The output format is not yet supported")
