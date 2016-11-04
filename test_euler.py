#!/usr/bin/python

import unittest

from euler import EulerPrimeFinder

class TestProvidedCases(unittest.TestCase):
    """
    This is a little silly, admittedly. Could be condensed significantly
    by removing all the repetition and just feeding a test case with the
    provided values.

    Just wanted to run through all the provided test cases and flag the ones
    that fail, unittest test case function names provide useful feedback about
    which cases fail.
    """
    def setUp(self):
        self.finder = EulerPrimeFinder(1000)

    def test_3_3(self):
        x = 3
        y = 3
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 353)
        self.assertEqual(int(with_two_result[-1]['prime']), 523)

    def test_4_5(self):
        x = 4
        y = 5
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 24709)
        # This will fail; 24977 is the 3rd, not 4th, 5-digit prime
        self.assertEqual(int(with_two_result[-1]['prime']), 24977)

    def test_3_2(self):
        x = 3
        y = 2
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 23)
        self.assertEqual(int(with_two_result[-1]['prime']), 23)

    def test_1_4(self):
        x = 1
        y = 4
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 4523)
        self.assertEqual(int(with_two_result[-1]['prime']), 4523)

    def test_5_6(self):
        x = 5
        y = 6
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 995957)
        self.assertEqual(int(with_two_result[-1]['prime']), 995957)

    def test_9_6(self):
        x = 9
        y = 6
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 594571)
        self.assertEqual(int(with_two_result[-1]['prime']), 594571)

    def test_6_10(self):
        x = 6
        y = 10
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 1573834187)
        # This will fail; 1063686487 doesn't appear in the first 1000 digits
        self.assertEqual(int(with_two_result[-1]['prime']), 1063686487)

    def test_4_1(self):
        x = 4
        y = 1
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 5)
        self.assertEqual(int(with_two_result[-1]['prime']), 2)

    def test_3_5(self):
        x = 3
        y = 5
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 24977)
        # This will fail; 62497 is the 2nd, not 3rd, 5-digit prime
        self.assertEqual(int(with_two_result[-1]['prime']), 62497)

    def test_2_7(self):
        x = 2
        y = 7
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 2497757)
        self.assertEqual(int(with_two_result[-1]['prime']), 6028747)

    def test_8_3(self):
        x = 8
        y = 3
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 277)
        self.assertEqual(int(with_two_result[-1]['prime']), 967)

    def test_5_11(self):
        x = 5
        y = 11
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 33829880753)
        # This will fail; 36864870169 doesn't appear in the first 1000 digits
        self.assertEqual(int(with_two_result[-1]['prime']), 36864870169)

    def test_5_13(self):
        x = 5
        y = 13
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 3232862794349)
        # This will fail; 7099983170353 doesn't appear in the first 1000 digits
        self.assertEqual(int(with_two_result[-1]['prime']), 7099983170353)

    def test_6_12(self):
        x = 6
        y = 12
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 157383418793)
        # This will fail; 82449550453 doesn't appear in the first 1000 digits
        self.assertEqual(int(with_two_result[-1]['prime']), 82449550453)

    def test_7_6(self):
        x = 7
        y = 6
        without_two_result = self.finder.find_xth_prime_of_y_digits(x, y, False)
        with_two_result = self.finder.find_xth_prime_of_y_digits(x, y, True)

        self.assertEqual(int(without_two_result[-1]['prime']), 630353)
        self.assertEqual(int(with_two_result[-1]['prime']), 630353)

if __name__ == '__main__':
    unittest.main()