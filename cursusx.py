#!/usr/bin/env python
import sys

from model.parser.ParserModel import ParserFactory


def main():
    command: str = ' '.join(sys.argv[1:])
    print(command)
    print(ParserFactory[str]().from_command(
        input_command=command).execute_command(command).wrap_output())


if __name__ == "__main__":
    main()
