from typing import Callable
from commands.courses import *
from commands.command import Command


commands = {
    "course": {
        "add": AddCourseCommand,
        "remove": RemoveCourseCommand,
        "list": ListCoursesCommand
    }
}


def execute(*args: str):
    command = commands
    while True:
        if type(command) is not dict:
            break

        command = command.get(args[0])
        args = args[1:]

        if command == None:
            print("Command not found.")
            return

    if issubclass(command, Command):
        command()(args)
        return
