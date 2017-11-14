from solutions.reverse_int import Solution

class TestReverseInt(object):
    def setup(self):
        print "before class method"
        self.solution = Solution()

    def test_reverse_1_dig_int(self):
        assert self.solution.reverse(1) == 1

    def test_reverse_positive_int(self):
        assert self.solution.reverse(1234) == 4321

    def test_reverse_negative_int(self):
        assert self.solution.reverse(-6789) == -9876

    def test_reverse_with_zero_prefix(self):
        assert self.solution.reverse(1239000) == 9321
    
    def test_reverse_negative_with_zero_prefix(self):
        assert self.solution.reverse(-123900) == -9321
    def test_reverse_overflow(self):
        assert self.solution.reverse(2147483648) == 0