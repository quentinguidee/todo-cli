from typing import Any

from commands.command import Command


class AddCourseCommand(Command):
    args = {"name": "The course to add."}

    def execute(self, args) -> Any:
        print("ADDED {name}".format(name=args[0]))


class RemoveCourseCommand(Command):
    args = {"name": "The course to remove."}

    def execute(self, args) -> Any:
        print("REMOVED {name}".format(name=args[0]))


class ListCoursesCommand(Command):
    def execute(self, args) -> Any:
        print("LIST")
