from models.course import Course
from typing import Any

from commands.command import Command
import save


class AddCourseCommand(Command):
    args = {"name": "The course to add."}

    def execute(self, args) -> Any:
        id = "-".join(args[0].lower().split())
        save.add_course(Course(id, args[0]))
        print("ADDED {name}".format(name=args[0]))


class RemoveCourseCommand(Command):
    args = {"name": "The course to remove."}

    def execute(self, args) -> Any:
        save.remove_course(args[0])
        print("REMOVED {name}".format(name=args[0]))


class ListCoursesCommand(Command):
    def execute(self, args) -> Any:
        print(save.get_courses())
