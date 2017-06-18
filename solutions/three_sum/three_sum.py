class Solution(object):
    def two_sum(self, nums, target):
        look_dict = {}
        for i, v in enumerate(nums):
            try:
                return [nums[look_dict[target - v]], nums[i]]
            except KeyError:
                look_dict.setdefault(v, i)

    def three_sum(self, nums, target):
        result = []
        for i, v in enumerate(nums):
            new_num = nums[0:i] + nums[i + 1:]
            the_other_two = self.two_sum(new_num, target - v)
            if the_other_two:
                return [i] + [nums.index(v) for v in the_other_two]
