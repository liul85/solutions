import unittest

from nose.tools import assert_equal
from solutions.roman_integer import Solution

class RomanToIntegerTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicRomanNumberConvertions(self):
        assert_equal(self.solution.roman_to_integer("I"), 1)
        assert_equal(self.solution.roman_to_integer("II"), 2)
        assert_equal(self.solution.roman_to_integer("III"), 3)
        assert_equal(self.solution.roman_to_integer("IV"), 4)
        assert_equal(self.solution.roman_to_integer("VII"), 7)
        assert_equal(self.solution.roman_to_integer("IX"), 9)
        assert_equal(self.solution.roman_to_integer("XXX"), 30)
        assert_equal(self.solution.roman_to_integer("XL"), 40)
        assert_equal(self.solution.roman_to_integer("XLIV"), 44)
        assert_equal(self.solution.roman_to_integer("LXX"), 70)
        assert_equal(self.solution.roman_to_integer("XC"), 90)
        assert_equal(self.solution.roman_to_integer("CCXLVIII"), 248)
        assert_equal(self.solution.roman_to_integer("CCC"), 300)
        assert_equal(self.solution.roman_to_integer("CD"), 400)
        assert_equal(self.solution.roman_to_integer("DXLIX"), 549)
        assert_equal(self.solution.roman_to_integer("MCMLIV"), 1954)