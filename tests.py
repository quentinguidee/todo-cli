from tests.test_courses import TestCourses
import unittest


def tests_suite():
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestCourses)
    ])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(tests_suite())
