import time
import datetime


class Time:
    def __init__(self, timestamp: float):
        self.timestamp = timestamp

    @classmethod
    def now(cls):
        return cls(time.time())

    def get_hour_and_minutes(self, timezone=None) -> str:
        now = datetime.datetime.fromtimestamp(self.timestamp, tz=timezone)
        return "{hour:02d}:{min:02d}".format(hour=now.hour, min=now.minute)

    def get_date(self) -> str:
        return datetime.date.fromtimestamp(self.timestamp).isoformat()

    def __eq__(self, other: 'Time') -> bool:
        return self.timestamp == other.timestamp


class DeltaTime:
    def __init__(self, timestamp: float):
        self.timestamp = timestamp

    def get_hour_minutes_seconds(self):
        return str(time.strftime('%H:%M:%S', time.gmtime(self.timestamp)))

    @classmethod
    def between(cls, a: Time, b: Time):
        return cls(abs(b.timestamp - a.timestamp))

    def __add__(self, other: 'DeltaTime'):
        self.timestamp += other.timestamp
        return self

    def __eq__(self, other: 'DeltaTime') -> bool:
        return self.timestamp == other.timestamp
