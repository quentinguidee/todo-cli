import save
import datetime

from rich.console import Console
from rich.text import Text

from commands.command import Command
from utils.time import DeltaTime, Time


class StartTimerCommand(Command):
    def execute(self, args):
        now = Time.now()

        save.start_timer(now.timestamp)

        console = Console()
        tag = Text(" TIMER STARTED ", style="bold black on green", end=" ")
        console.print(tag, Text("It is " + now.get_hour_and_minutes()))


class StopTimerCommand(Command):
    def execute(self, args):
        start_timer = Time(save.get_current_timer())
        end_timer = Time.now()
        elapsed_time = DeltaTime.between(end_timer, start_timer)

        save.add_current_study(end_timer.get_date(), start_timer, end_timer)
        save.end_timer()

        console = Console()
        tag = Text(" TIMER STOPPED ", style="bold black on green", end=" ")
        message = Text("It is " + end_timer.get_hour_and_minutes() +
                       " and you worked " + elapsed_time.get_hour_minutes_seconds())
        console.print(tag, message)
