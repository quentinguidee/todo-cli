import time
import save
import datetime

from rich.console import Console
from rich.text import Text

from commands.command import Command


def get_now():
    return "It is {hour}:{min}".format(hour=datetime.datetime.now().hour, min=datetime.datetime.now().minute)


class StartTimerCommand(Command):
    def execute(self, args):
        save.start_timer(time.time())

        console = Console()
        tag = Text(" TIMER STARTED ", style="bold black on green", end=" ")
        console.print(tag, Text(get_now()))


class StopTimerCommand(Command):
    def execute(self, args):
        start_timer = save.get_current_timer()
        end_timer = time.time()
        elapsed_time = end_timer - start_timer

        save.add_current_study(datetime.date.today().isoformat(), start_timer, end_timer)
        save.end_timer()

        console = Console()
        tag = Text(" TIMER STOPPED ", style="bold black on green", end=" ")
        elapsed_time = str(time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
        console.print(tag, Text(get_now() + " and you worked " + elapsed_time))
