# coding=utf-8

import unittest
from ucnumber import validate


class ValidationTests(unittest.TestCase):

    def test_validation_as_string(self):
        self.assertTrue(validate('14644088'))

    def test_validation_as_number(self):
        self.assertTrue(validate(14644088))

    def test_validation_as_string_with_J(self):
        self.assertTrue(validate('1263476J'))

    def test_validation_as_string_with_digit_11(self):
        self.assertTrue(validate('18640850'))

    def test_fail_on_invalid_number(self):
        self.assertFalse(validate(12635662))

    def test_fail_on_invalid_number_format(self):
        self.assertFalse(validate('A!CDEFG@'))

    def test_fail_on_blank_input(self):
        self.assertFalse(validate(''))
        self.assertFalse(validate(None))

    def test_fail_on_big_numbers(self):
        from sys import maxsize
        self.assertFalse(validate(maxsize))


if __name__ == '__main__':
    unittest.main()
