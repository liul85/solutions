class Solution(object):
    def isPalindrome(self, num):
        if num < 0: return False
        if int("".join(list(str(num))[::-1])) == num:
            return True
        return False