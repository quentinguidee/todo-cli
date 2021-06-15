from unittest import TestCase


from models.event import Event
from utils.time import Time


class TestEvent(TestCase):
    def test_event(self):
        event = Event("2", Time(1623767280.837653), Time(1623767283.525394))
        self.assertEqual(event.id, "2")
        self.assertEqual(event.start.timestamp, Time(1623767280.837653).timestamp)
        self.assertEqual(event.end.timestamp, Time(1623767283.525394).timestamp)
