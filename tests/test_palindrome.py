from solutions.palindrome import Solution

class TestPalindrome(object):
    def setup(self):
        self.solution = Solution()

    def test_negative_num(self):
        assert self.solution.isPalindrome(-121) == False

    def test_positive_num(self):
        assert self.solution.isPalindrome(1234321) == True

    def test_single_num(self):
        assert self.solution.isPalindrome(0) == True