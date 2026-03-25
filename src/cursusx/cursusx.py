#!/usr/bin/env python
import sys

from cursusx.model.cli.command.OutputModel import AbstractOutput
from cursusx.model.parser.ParserModel import ParserFactory
from cursusx.wrapper.CursusxViewerApp import CursusxViewerApp
from cursusx.wrapper.ViewCommandFactory import get_viewer_command_widget

PRETTY_OUTPUT = "pretty"

special_pre_command: set[str] = {PRETTY_OUTPUT}


def main():
    start_command_index: int = 2 if sys.argv[1] in special_pre_command else 1
    command: str = ' '.join(sys.argv[start_command_index:])
    output: AbstractOutput = ParserFactory[str]().from_command(
        input_command=command).execute_command(command)
    if sys.argv[1] == PRETTY_OUTPUT:
        CursusxViewerApp(get_viewer_command_widget(output)).run()


if __name__ == "__main__":
    main()
