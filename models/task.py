from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    NOT_DONE = 0
    ALMOST_DONE = 1
    DONE = 2

    def get_glyph(self):
        if self == self.NOT_DONE:
            return "✗"
        if self == self.ALMOST_DONE:
            return "~"
        if self == self.DONE:
            return "✓"

    def get_color(self):
        if self == self.NOT_DONE:
            return "red"
        if self == self.ALMOST_DONE:
            return "orange"
        if self == self.DONE:
            return "green"


@dataclass
class Task:
    id: str
    name: str
    status: TaskStatus = TaskStatus.NOT_DONE
