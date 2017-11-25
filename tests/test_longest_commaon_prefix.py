from solutions.longest_commaon_prefix import Solution

class TestLongestComPrefix(object):
    def setup(self):
        self.solution = Solution()

    def test_happy_pass(self):
        assert self.solution.get_common_prefix(["abc", "abc"]) == "abc"
    
    def test_has_less_one(self):
        assert self.solution.get_common_prefix(["abc", "abddef", "abhk"]) == "ab"

    def test_has_no_common_prefix(self):
        assert self.solution.get_common_prefix(["abc", "aef", "bbc"]) == ""
    
    def test_empty_str_list(self):
        assert self.solution.get_common_prefix([]) == ""