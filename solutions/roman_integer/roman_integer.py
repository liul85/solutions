class Solution(object):
    def roman_to_integer(self, roman):
        """ convert roman number to integer """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        reversed_roman = roman[::-1]
        int_sum = mapping[reversed_roman[0]]
        last_sym = reversed_roman[0]
        for i, r in enumerate(reversed_roman[1:]):
            if mapping[r] >= mapping[last_sym]:
                int_sum += mapping[r]
            else:
                int_sum -= mapping[r]
            last_sym = r
        return int_sum