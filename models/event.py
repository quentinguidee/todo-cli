from dataclasses import dataclass

from utils.time import Time


@dataclass
class Event:
    id: str
    start: Time
    end: Time
    course_id: str
