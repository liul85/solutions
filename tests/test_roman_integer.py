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
        assert self.solution.roman_to_integer("XIV") == 14
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

    def testIntegerToRoman(self):
        assert self.solution.integer_to_roman(1) == "I"
        assert self.solution.integer_to_roman(2) == "II"
        assert self.solution.integer_to_roman(4) == "IV"
        assert self.solution.integer_to_roman(5) == "V"
        assert self.solution.integer_to_roman(7) == "VII"
        assert self.solution.integer_to_roman(9) == "IX"
        assert self.solution.integer_to_roman(10) == "X"
        assert self.solution.integer_to_roman(23) == "XXIII"
        assert self.solution.integer_to_roman(44) == "XLIV"
        assert self.solution.integer_to_roman(99) == "XCIX"
        assert self.solution.integer_to_roman(101) == "CI"
        assert self.solution.integer_to_roman(444) == "CDXLIV"
        assert self.solution.integer_to_roman(999) == "CMXCIX"
        assert self.solution.integer_to_roman(1444) == "MCDXLIV"