import pytz

from unittest import TestCase

from utils.time import DeltaTime, Time


class TestTime(TestCase):
    def test_time(self):
        time = Time(1623766147.58488)
        self.assertEqual(time.get_date(), "2021-06-15")
        self.assertEqual(time.get_hour_and_minutes(pytz.UTC), "14:09")
        self.assertEqual(time.timestamp, 1623766147.58488)

    def test_time_now(self):
        time = Time.now()
        self.assertIsInstance(time.timestamp, float)

    def test_eq_time(self):
        time_a = Time(2000)
        time_b = Time(2000)
        time_c = Time(3500)

        self.assertEqual(time_a, time_b)
        self.assertNotEqual(time_a, time_c)

    def test_delta_time(self):
        delta_time = DeltaTime(10000)
        self.assertEqual(delta_time.get_hour_minutes_seconds(), "02:46:40")
        self.assertEqual(delta_time.timestamp, 10000)

    def test_delta_time_between(self):
        time_a = Time.now()
        time_b = Time(time_a.timestamp + 2000)
        delta_time = DeltaTime.between(time_a, time_b)
        self.assertEqual(delta_time.timestamp, 2000)

    def test_eq_delta_time(self):
        delta_time_a = DeltaTime(2000)
        delta_time_b = DeltaTime(2000)
        delta_time_c = DeltaTime(3500)

        self.assertEqual(delta_time_a, delta_time_b)
        self.assertNotEqual(delta_time_a, delta_time_c)

    def test_sum_delta_time(self):
        delta_time_a = DeltaTime(1000)
        delta_time_b = DeltaTime(2000)

        total = delta_time_a + delta_time_b
        expect = DeltaTime(3000)

        self.assertEqual(total.timestamp, expect.timestamp)
