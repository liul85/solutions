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

    def integer_to_roman(self, number):
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        M = ["", "M", "MM", "MMM"]
        return M[(number%10000)/1000] + C[(number%1000)/100] + X[(number%100)/10] + I[number % 10]
        