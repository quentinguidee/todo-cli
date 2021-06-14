from typing import Callable
from commands.courses import *
from commands.command import Command


commands = {
    "course": {
        "add": AddCourseCommand(),
        "remove": RemoveCourseCommand(),
        "list": ListCoursesCommand(),
        "add-labo": AddTaskToCourseCommand("labo", "Labo"),
        "add-chapter": AddTaskToCourseCommand("chapter", "Chapter"),
        "add-session": AddTaskToCourseCommand("session", "Session"),
        "add-course": AddTaskToCourseCommand("course", "Course"),
        "list-tasks": ListTasksCourseCommand(),
        "set-status": SetStatusTaskCourseCommand(),
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

    if issubclass(type(command), Command):
        command(args)
        return
