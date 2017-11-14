from solutions.roman_integer import Solution

class TestRomanToInteger(object):
    def setup(self):
        self.solution = Solution()

    def testBasicRomanNumberConvertions(self):
        assert self.solution.roman_to_integer("II") == 2
        assert self.solution.roman_to_integer("III") == 3
        assert self.solution.roman_to_integer("I") == 1
        assert self.solution.roman_to_integer("IV") == 4
        assert self.solution.roman_to_integer("VII") == 7
        assert self.solution.roman_to_integer("IX") == 9
        assert self.solution.roman_to_integer("XXX") == 30
        assert self.solution.roman_to_integer("XL") == 40
        assert self.solution.roman_to_integer("XLIV") == 44
        assert self.solution.roman_to_integer("LXX") == 70
        assert self.solution.roman_to_integer("XC") == 90
        assert self.solution.roman_to_integer("CCXLVIII") == 248
        assert self.solution.roman_to_integer("CCC") == 300
        assert self.solution.roman_to_integer("CD") == 400
        assert self.solution.roman_to_integer("DXLIX") == 549
        assert self.solution.roman_to_integer("MCMLIV") == 1954
