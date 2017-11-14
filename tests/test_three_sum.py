from solutions.three_sum import Solution

class TestThreeSum(object):
    def setup(self):
        self.solution = Solution()

    def test_three_sum_all_positive(self):
        nums = [1, 2, 3, 4, 5, 6]
        target = 12
        assert self.solution.three_sum(nums, target) == [0, 4, 5]

    def test_three_sum_with_negative(self):
        nums = [1, -2, 3, -4, 5, 6]
        target = 3
        assert self.solution.three_sum(nums, target) == [0, 3, 5]

    def test_three_sum_with_duplicated(self):
        nums = [3, 3, 3, -3, 5, 6]
        target = 6
        assert self.solution.three_sum(nums, target) == [0, 3, 5]
    
    def test_three_sum_with_no_matched(self):
        nums = [1, 2, 3, -3, 5, 6]
        target = 19
        assert self.solution.three_sum(nums, target) == None
