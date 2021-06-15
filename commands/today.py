import save
import datetime

from rich.console import Console
from rich.table import Table
from rich.text import Text

from commands.command import Command
from models.event import Event
from utils.time import DeltaTime, Time


class TodayCommand(Command):
    def execute(self, args):
        events: list[Event] = save.get_events(Time.now())

        console = Console()

        table = Table(title="Events")

        table.add_column("Duration")
        table.add_column("Start")
        table.add_column("End")

        total = DeltaTime(0)

        for event in events:
            delta_time = DeltaTime.between(event.start, event.end)
            total += delta_time
            table.add_row(
                delta_time.get_hour_minutes_seconds(),
                event.start.get_hour_and_minutes(),
                event.end.get_hour_and_minutes()
            )

        tag = Text(" TOTAL ", style="bold black on yellow", end=" ")

        console.print(table, Text(end=" "), tag, Text(total.get_hour_minutes_seconds()))
