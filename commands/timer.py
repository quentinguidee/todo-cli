
import datetime
from typing import NoReturn

from rich.console import Console
from rich.text import Text

from commands.command import Command
from utils.time import DeltaTime, Time
import save


class StartTimerCommand(Command):
    args = {"course_id": "The course to study."}

    def execute(self, args) -> NoReturn:
        now = Time.now()

        save.start_timer(now.timestamp, args[0])

        console = Console()
        tag = Text(" TIMER STARTED ", style="bold black on green", end=" ")
        console.print(tag, Text(f"It is {now.get_hour_and_minutes()}"))


class StopTimerCommand(Command):
    def execute(self, args) -> NoReturn:
        temp_timer = save.get_current_timer()
        start = temp_timer.get("start")
        course_id = temp_timer.get("course_id")

        start_timer = Time(start)
        end_timer = Time.now()
        elapsed_time = DeltaTime.between(end_timer, start_timer)

        save.add_current_study(end_timer.get_date(), start_timer, end_timer, course_id)
        save.end_timer()

        console = Console()
        tag = Text(" TIMER STOPPED ", style="bold black on green", end=" ")
        message = Text("It is {} and you worked {}".format(
            end_timer.get_hour_and_minutes(),
            elapsed_time.get_hour_minutes_seconds()))

        console.print(tag, message)
