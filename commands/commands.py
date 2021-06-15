from commands.command import Command
from commands.courses import *
from commands.timer import *


commands = {
    "course": {
        "add": AddCourseCommand(),
        "remove": RemoveCourseCommand(),
        "list": ListCoursesCommand(),
        "add-lab": AddTaskToCourseCommand("lab", "Lab"),
        "add-chapter": AddTaskToCourseCommand("chapter", "Chapter"),
        "add-session": AddTaskToCourseCommand("session", "Session"),
        "add-course": AddTaskToCourseCommand("course", "Course"),
        "remove-task": RemoveTaskCourseCommand(),
        "list-tasks": ListTasksCourseCommand(),
        "set-status": SetStatusTaskCourseCommand(),
    },
    "timer": {
        "start": StartTimerCommand(),
        "stop": StopTimerCommand(),
    }
}


def execute(*args: str):
    command = commands
    while True:
        if not isinstance(command, dict):
            break

        command = command.get(args[0])
        args = args[1:]

        if command is None:
            print("Command not found.")
            return

    if issubclass(type(command), Command):
        command(args)
        return
