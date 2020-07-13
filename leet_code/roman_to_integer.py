"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
steps:
1. Split the Roman Numeral string into Roman Symbols (character).
2. Convert each symbol of Roman Numerals into the value it represents.
3. Take symbol one by one from starting from index 0:
4. If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
5. else subtract this value by adding the value of next symbol to the running total.
"""


class Solution:
    def romanToInt(self, s):
        number = []
        new_string = list(s)
        integer = []
        new_number = 0
        j = 1
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        for i in new_string:
            value = roman.get(i)
            number.append(value)
        for num in number:
            if j == len(number):
                new_number = new_number + num
                integer.append(new_number)
                break;
            if num >= number[j]:
                new_number = new_number + num
                integer.append(new_number)
            else:
                new_number = new_number + (number[j] - num)
                integer.append(new_number)
                number.remove(number[j])

            j=j+1
        return integer[-1]




object = Solution()
print(object.romanToInt("MMDXXV"))
