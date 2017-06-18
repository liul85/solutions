class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_dict = {}
        for i, v in enumerate(nums):
            try:
                return [look_dict[target - v], i]
            except KeyError:
                look_dict.setdefault(v, i)
