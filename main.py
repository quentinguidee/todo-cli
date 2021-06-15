import sys

from commands.commands import execute


def exec():
    execute(*sys.argv[1:])


if __name__ == "__main__":
    exec()
