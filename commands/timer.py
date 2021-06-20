from models.task import TaskStatus
from os import name
import platform

from typing import NoReturn

from rich.console import Console
from rich.text import Text
from PyInquirer import prompt

from commands.command import Command
from utils.time import DeltaTime, Time
from apple.calendar import save_event_to_calendar
import save


OS = platform.system()


class StartTimerCommand(Command):
    args = {
        "course_id": "The course to study.",
        "task_id": "The task to study.",
    }

    def execute(self, args) -> NoReturn:
        now = Time.now()
        course_id, task_id = args

        save.start_timer(now.timestamp, course_id, task_id)

        console = Console()
        tag = Text(" TIMER STARTED ", style="bold black on green", end=" ")
        console.print(tag, Text(f"It is {now.get_hour_and_minutes()}"))


class StopTimerCommand(Command):
    def save_event(self, start_timer: Time, end_timer: Time, course_id: str, task_id: str):
        save.add_current_study(end_timer.get_date(), start_timer, end_timer, course_id, task_id)

    def stop_timer(self):
        save.end_timer()

    def ask_task_status(self, course_id: str, task_id: str):
        responses = {
            "Yes": 2,
            "No, but almost": 1,
            "Not at all": 0,
        }

        question = [{
            "type": "list",
            "name": "status",
            "message": "Did you finished your task?",
            "choices": responses.keys()
        }]

        response = prompt(question)
        status = response.get("status")

        save.set_task_status(course_id, task_id, TaskStatus(responses[status]))

    def create_event(self, elapsed_time: DeltaTime, course_id: str, task_id: str):
        if OS == "Darwin":
            event_name = "{course} {task}".format(
                course=save.get_course(course_id).name,
                task=save.get_task(course_id, task_id).name)

            save_event_to_calendar(
                name=event_name,
                duration=elapsed_time.timestamp)

    def display(self, end_timer: Time, elapsed_time: DeltaTime):
        console = Console()
        tag = Text(" TIMER STOPPED ", style="bold black on green", end=" ")
        message = Text("It is {} and you worked {}".format(
            end_timer.get_hour_and_minutes(),
            elapsed_time.get_hour_minutes_seconds()))

        console.print(tag, message)

    def execute(self, args) -> NoReturn:
        temp_timer = save.get_current_timer()

        start = temp_timer.get("start")
        course_id = temp_timer.get("course_id")
        task_id = temp_timer.get("task_id")

        start_timer = Time(start)
        end_timer = Time.now()
        elapsed_time = DeltaTime.between(end_timer, start_timer)

        self.save_event(start_timer, end_timer, course_id, task_id)
        self.stop_timer()

        self.ask_task_status(course_id, task_id)

        self.create_event(elapsed_time, course_id, task_id)
        self.display(end_timer, elapsed_time)
