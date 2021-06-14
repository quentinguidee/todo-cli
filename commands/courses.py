import save

from rich import console
from rich import text

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

from models.course import Course
from typing import Any

from commands.command import Command

from models.task import Task


class AddCourseCommand(Command):
    args = {"name": "The course to add."}

    def execute(self, args) -> None:
        id = "-".join(args[0].lower().split())
        save.add_course(Course(id, args[0]))

        console = Console()
        tag = Text(" COURSE ADDED ", style="bold black on green", end=" ")
        console.print(tag, Text(args[0]))


class RemoveCourseCommand(Command):
    args = {"name": "The course to remove."}

    def execute(self, args) -> None:
        save.remove_course(args[0])

        console = Console()
        tag = Text(" COURSE REMOVED ", style="bold black on green", end=" ")
        console.print(tag, Text(args[0]))


class ListCoursesCommand(Command):
    def execute(self, args) -> None:
        courses = save.get_courses()

        console = Console()
        content = "\n".join(map(lambda course: "* " + course.name, courses))
        markdown = Markdown(content)

        console.print(markdown)


class AddTaskToCourseCommand(Command):
    def __init__(self, task_id: str, task_name: str) -> None:
        self.task_id = task_id
        self.task_name = task_name

    args = {
        "name": "The linked course.",
        "numbers": "The tasks ids."
    }

    def execute(self, args) -> None:
        def get_ids():
            ids: str = args[1]
            if ids.isdigit():
                return [ids]

            ids = ids.split("-")
            return range(int(ids[0]), int(ids[1]) + 1)

        tasks = [Task(
            "{name}{id}".format(name=self.task_id, id=id),
            "{name} {id}".format(name=self.task_name, id=id)
        ) for id in get_ids()]

        save.add_tasks(args[0], tasks)

        console = Console()
        for task in tasks:
            tag = Text(" TASK ADDED ", style="bold black on green", end=" ")
            console.print(tag, Text(task.name))
