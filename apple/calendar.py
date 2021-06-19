import subprocess

from math import floor
from os import remove
from subprocess import run
from rich.console import Console
from rich.progress import BarColumn, Progress


def save_event_to_calendar(name: str, duration: float):
    with Progress("[progress.description]{task.description}", BarColumn()) as progress:
        progress.add_task("Adding event to calendar", start=False)

        duration = floor(duration)
        with open("apple/duration", "w") as f:
            f.write(str(duration))

        with open("apple/name", "w") as f:
            f.write(name)

        run(["osascript", "apple/events.applescript"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)

        remove("apple/duration")
        remove("apple/name")
