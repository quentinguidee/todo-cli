from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    NOT_DONE = 0
    ALMOST_DONE = 1
    DONE = 2

    def get_glyph(self):
        return {
            self.NOT_DONE: "✗",
            self.ALMOST_DONE: "~",
            self.DONE: "✓",
        }.get(self)

    def get_color(self):
        return {
            self.NOT_DONE: "red",
            self.ALMOST_DONE: "yellow",
            self.DONE: "green"
        }.get(self)

    @classmethod
    def from_string(cls, string: str):
        return {
            "not-done": cls.NOT_DONE,
            "almost-done": cls.ALMOST_DONE,
            "done": cls.DONE,
        }.get(string)


@dataclass
class Task:
    id: str
    name: str
    status: TaskStatus = TaskStatus.NOT_DONE
