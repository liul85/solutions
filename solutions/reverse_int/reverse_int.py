class Solution(object):
    def reverse(self, num):
        s = cmp(num, 0)
        r = int(`s*num`[::-1])
        return s*r*(r<2**31)