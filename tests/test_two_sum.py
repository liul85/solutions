import unittest
from nose.tools import assert_equal
from solutions.two_sum import Solution


class TwoNumTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum_all_positive(self):
        nums = [3, 13, 24, 5]
        target = 8
        assert_equal(self.solution.two_sum(nums, target), [0, 3])

    def test_two_sum_with_negative(self):
        nums = [13, 3, -5, 9]
        target = 8
        assert_equal(self.solution.two_sum(nums, target), [0, 2])

    def test_two_sum_with_duplicated(self):
        nums = [3, 4, 3, 6]
        target = 6
        assert_equal(self.solution.two_sum(nums, target), [0, 2])

    def test_two_sum_with_no_matched_items(self):
        nums = [1, 2, 3, 4]
        target = 8
        assert_equal(self.solution.two_sum(nums, target), None)

if __name__ == "__main__":
    unittest.main()
