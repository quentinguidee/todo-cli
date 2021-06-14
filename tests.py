import sys
import unittest

from unittest.loader import TestLoader

from tests.test_courses import TestCourses
from tests.test_storage import TestStorage


def tests_suite():
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestStorage),
        unittest.TestLoader().loadTestsFromTestCase(TestCourses)
    ])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    success = runner.run(tests_suite()).wasSuccessful()
    sys.exit(1 if not success else 0)
