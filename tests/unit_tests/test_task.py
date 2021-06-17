from unittest import TestCase


from models.task import Task, TaskStatus


class TestTaskStatus(TestCase):
    def test_task_glyph(self):
        glyphs = {
            TaskStatus.NOT_DONE: "✗",
            TaskStatus.ALMOST_DONE: "~",
            TaskStatus.DONE: "✓",
        }

        for k, v in glyphs.items():
            self.assertEqual(k.glyph, v)

    def test_task_color(self):
        colors = {
            TaskStatus.NOT_DONE: "red",
            TaskStatus.ALMOST_DONE: "yellow",
            TaskStatus.DONE: "green",
        }

        for k, v in colors.items():
            self.assertEqual(k.color, v)

    def test_from_string(self):
        strings = {
            "not-done": TaskStatus.NOT_DONE,
            "almost-done": TaskStatus.ALMOST_DONE,
            "done": TaskStatus.DONE
        }

        for k, v in strings.items():
            self.assertEqual(TaskStatus.from_string(k), v)


class TestTask(TestCase):
    def test_task(self):
        task = Task("id", "Name", TaskStatus.DONE)
        self.assertEqual(task.id, "id")
        self.assertEqual(task.name, "Name")
        self.assertEqual(task.status, TaskStatus.DONE)
