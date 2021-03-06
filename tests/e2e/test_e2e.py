import json
import os
import sys
import io

from datetime import date
from shlex import split
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from commands.timer import StopTimerCommand
from main import exec

TEMP_FILE_NAME = "save-temp.json"


def execute(command: str):
    sys.argv = split(command)
    exec()


def get_json(filename: str):
    with open(filename, 'r') as f:
        return json.load(f)


def get_expected_save(id: str):
    return get_json('tests/e2e/expected/expected_{id}.json'.format(id=id))


def get_current_save():
    return get_json(TEMP_FILE_NAME)


class TestE2E(TestCase):
    @patch.object(StopTimerCommand, "ask_task_status", new=Mock())
    @patch("storage.SAVE_FILENAME", TEMP_FILE_NAME)
    @patch("commands.timer.OS", "None")
    @patch("sys.stdout", io.StringIO())
    def test_end_to_end(self):
        execute('todo course add Physics')
        execute('todo course add Mathematics')
        execute('todo course add English')
        execute('todo course remove Mathematics')
        execute('todo course list')

        data, expect = get_current_save(), get_expected_save("A")
        self.assertDictEqual(data, expect)

        execute('todo course add-lab physics 1-3')
        execute('todo course add-chapter physics 1-3')
        execute('todo course add-session english 1-3')
        execute('todo course add-course physics 2')
        execute('todo course remove-task physics lab2')

        data, expect = get_current_save(), get_expected_save("B")
        self.assertDictEqual(data, expect)

        execute('todo course set-status physics lab1 done')
        execute('todo course set-status english session1 almost-done')
        execute('todo course set-status english session3 done')
        execute('todo course set-status english session3 not-done')

        execute('todo course list-tasks english')
        execute('todo course list-all-tasks')

        data, expect = get_current_save(), get_expected_save("C")
        self.assertDictEqual(data, expect)

        execute('todo timer start physics lab1')
        execute('todo timer stop')

        data = get_current_save()
        self.assertIn("timer", data)

        timer = data.get("timer")
        self.assertIn("events", timer)

        events = timer.get("events")
        today = date.today().isoformat()
        self.assertIn(today, events)

        today = events.get(today)
        self.assertIn("1", today)

        event = today.get("1")
        start, end, course_id = event.get("start"), event.get("end"), event.get("course_id")
        self.assertIsInstance(start, float)
        self.assertIsInstance(end, float)
        self.assertEqual(course_id, "physics")

        execute('todo timer start english session1')
        execute('todo timer stop')

        data = get_current_save()

        self.assertIn("2", data.get("timer").get("events").get(date.today().isoformat()))

        execute('todo today')

    def tearDown(self):
        os.remove(TEMP_FILE_NAME)
