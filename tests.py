import sys
import unittest

from tests.e2e.test_e2e import TestE2E

from tests.unit_tests.test_storage import TestStorage


def tests_suite():
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestStorage),
        unittest.TestLoader().loadTestsFromTestCase(TestE2E),
    ])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    success = runner.run(tests_suite()).wasSuccessful()
    sys.exit(1 if not success else 0)
