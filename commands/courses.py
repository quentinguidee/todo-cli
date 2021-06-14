from rich import console
from rich import text
import save

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

from models.course import Course
from typing import Any

from commands.command import Command


class AddCourseCommand(Command):
    args = {"name": "The course to add."}

    def execute(self, args) -> Any:
        id = "-".join(args[0].lower().split())
        save.add_course(Course(id, args[0]))

        console = Console()
        tag = Text(" COURSE ADDED ", style="bold black on green", end=" ")
        console.print(tag, Text(args[0]))


class RemoveCourseCommand(Command):
    args = {"name": "The course to remove."}

    def execute(self, args) -> Any:
        save.remove_course(args[0])

        console = Console()
        tag = Text(" COURSE REMOVED ", style="bold black on green", end=" ")
        console.print(tag, Text(args[0]))


class ListCoursesCommand(Command):
    def execute(self, args) -> Any:
        courses = save.get_courses()

        console = Console()
        content = "\n".join(map(lambda course: "* " + course.name, courses))
        markdown = Markdown(content)

        console.print(markdown)
