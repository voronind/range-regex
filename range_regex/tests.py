import unittest
from range_regex import bounded_regex_for_range, regex_for_range


class RegexForRangeTest(unittest.TestCase):
    def _verify_range(self, regex, min_, max_, from_min_, to_max_):
        for nr in range(from_min_, to_max_ + 1):
            if min_ <= nr <= max_:
                self.assertRegexpMatches(str(nr), regex)
            else:
                self.assertNotRegexpMatches(str(nr), regex)

    def test_quality(self):
        self.assertEqual(regex_for_range(1, 1), '1')
        self.assertEqual(regex_for_range(65666, 65667), '6566[6-7]')
        self.assertEqual(regex_for_range(12, 3456), r'1[2-9]|[2-9]\d|[1-9]\d{2}|[1-2]\d{3}|3[0-3]\d{2}|34[0-4]\d|345[0-6]')

    def test_equal(self):
        regex = bounded_regex_for_range(1, 1)
        self._verify_range(regex, 1, 1, 0, 100)

    def test_equal_2(self):
        regex = bounded_regex_for_range(65443, 65443)
        self._verify_range(regex, 65443, 65443, 65000, 66000)

    def test_equal_3(self):
        regex = bounded_regex_for_range(192, 100020000300000)
        self._verify_range(regex, 192, 1000, 0, 1000)
        self._verify_range(regex, 100019999300000, 100020000300000, 100019999300000, 100020000400000)

    def test_repeated_digit(self):
        regex = bounded_regex_for_range(10331, 20381)
        self._verify_range(regex, 10331, 20381, 0, 99999)

    def test_repeated_zeros(self):
        regex = bounded_regex_for_range(10031, 20081)
        self._verify_range(regex, 10031, 20081, 0, 99999)

    def test_zero_one(self):
        regex = bounded_regex_for_range(10301, 20101)
        self._verify_range(regex, 10301, 20101, 0, 99999)

    def test_different_len_numbers_1(self):
        regex = bounded_regex_for_range(1030, 20101)
        self._verify_range(regex, 1030, 20101, 0, 99999)

    def test_repetead_one(self):
        regex = bounded_regex_for_range(102, 111)
        self._verify_range(regex, 102, 111, 0, 1000)

    def test_small_diff_1(self):
        regex = bounded_regex_for_range(102, 110)
        self._verify_range(regex, 102, 110, 0, 1000)

    def test_small_diff_2(self):
        regex = bounded_regex_for_range(102, 130)
        self._verify_range(regex, 102, 130, 0, 1000)

    def test_random_range_1(self):
        regex = bounded_regex_for_range(4173, 7981)
        self._verify_range(regex, 4173, 7981, 0, 99999)

    def test_one_digit_numbers(self):
        regex = bounded_regex_for_range(3, 7)
        self._verify_range(regex, 3, 7, 0, 99)

    def test_one_digit_at_bounds(self):
        regex = bounded_regex_for_range(1, 9)
        self._verify_range(regex, 1, 9, 0, 1000)

    def test_power_of_ten(self):
        regex = bounded_regex_for_range(1000, 8632)
        self._verify_range(regex, 1000, 8632, 0, 99999)

    def test_different_len_numbers_2(self):
        regex = bounded_regex_for_range(13, 8632)
        self._verify_range(regex, 13, 8632, 0, 10000)

    def test_different_len_numbers_small_diff(self):
        regex = bounded_regex_for_range(9, 11)
        self._verify_range(regex, 9, 11, 0, 100)

    def test_different_len_zero_eight_nine(self):
        regex = bounded_regex_for_range(90, 980099)
        self._verify_range(regex, 90, 980099, 0, 999999)

    def test_small_diff(self):
        regex = bounded_regex_for_range(19, 21)
        self._verify_range(regex, 19, 21, 0, 100)

    def test_different_len_zero_one_nine(self):
        regex = bounded_regex_for_range(999, 10000)
        self._verify_range(regex, 999, 10000, 1, 20000)


if __name__ == '__main__':
    unittest.main()
