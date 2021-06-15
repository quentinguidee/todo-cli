from unittest import TestCase


from models.course import Course


class TestCourse(TestCase):
    def test_course(self):
        course = Course("id", "Name")
        self.assertEqual(course.id, "id")
        self.assertEqual(course.name, "Name")
