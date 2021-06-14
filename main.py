import sys

from commands.commands import execute


if __name__ == "__main__":
    execute(*sys.argv[1:])
