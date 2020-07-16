'''

From Andrew Candela's lecture on 7-16-2020

https://leetcode.com/problems/integer-to-roman/

Given an int, convert to a roman string.
Given int should be between 1 and 3999.
'''


class NumOutOfBoundsException(Exception):
    pass


class Solution:

    def intToRoman(self, num):
        numeral_to_roman_map = {
            0: {
                0: '',
                1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX'
            },
            1: {
                0: '',
                1: 'X',
                2: 'XX',
                3: 'XXX',
                4: 'XL',
                5: 'L',
                6: 'LX',
                7: 'LXX',
                8: 'LXXX',
                9: 'XC'
            },
            2: {
                0: '',
                1: 'C',
                2: 'CC',
                3: 'CCC',
                4: 'CD',
                5: 'D',
                6: 'DC',
                7: 'DCC',
                8: 'DCCC',
                9: 'CM'
            },
            3: {
                0: '',
                1: 'M',
                2: 'MM',
                3: 'MMM'
            }
        }

        if num < 1 or num > 3999:
            raise NumOutOfBoundsException(
                f'You gave me a number outside of the range.')

        num_str = str(num)

        # For changing the index created by enumerate into the exponent of the digit (the power of 10)
        len_num = len(num_str) - 1

        exponent_num_list = [(len_num - index, int(num_digit))
                             for index, num_digit in enumerate(num_str)]
        # print(exponent_num_list)
        return ''.join([numeral_to_roman_map[exp][digit] for (exp, digit) in exponent_num_list])


s = Solution()
print(s.intToRoman(556))


class Solution2:
    def __init__(self):
        self.result = ""

    def intToRoman(self, num: int) -> str:
        if num >= 1000:
            num = num - 1000
            self.result += "M"
            self.intToRoman(num)
        elif num >= 900:
            num = num - 900
            self.result += "CM"
            self.intToRoman(num)
        elif num >= 500:
            num = num - 500
            self.result += "D"
            self.intToRoman(num)
        elif num >= 400:
            num = num - 400
            self.result += "CD"
            self.intToRoman(num)
        elif num >= 100:
            num = num - 100
            self.result += "C"
            self.intToRoman(num)
        elif num >= 90:
            num = num - 90
            self.result += "XC"
            self.intToRoman(num)
        elif num >= 50:
            num = num - 50
            self.result += "L"
            self.intToRoman(num)
        elif num >= 40:
            num = num - 40
            self.result += "XL"
            self.intToRoman(num)
        elif num >= 10:
            num = num - 10
            self.result += "X"
            self.intToRoman(num)
        elif num >= 9:
            num = num - 9
            self.result += "IX"
            self.intToRoman(num)
        elif num >= 5:
            num = num - 5
            self.result += "V"
            self.intToRoman(num)
        elif num >= 4:
            num = num - 4
            self.result += "IV"
            self.intToRoman(num)
        elif num >= 1:
            num = num - 1
            self.result += "I"
            self.intToRoman(num)
        else:
            print("finished")
        return self.result


s2 = Solution2()
print(s2.intToRoman(333))


class Solution3:

    def intToRoman(self, num: int) -> str:
        result = ''
        while num >= 1000:
            num = num - 1000
            result += "M"
        if num >= 900:
            num = num - 900
            result += "CM"
        if num >= 500:
            num = num - 500
            result += "D"
        if num >= 400:
            num = num - 400
            result += "CD"
        while num >= 100:
            num = num - 100
            result += "C"
        if num >= 90:
            num = num - 90
            result += "XC"
        if num >= 50:
            num = num - 50
            result += "L"
        if num >= 40:
            num = num - 40
            result += "XL"
        while num >= 10:
            num = num - 10
            result += "X"
        if num >= 9:
            num = num - 9
            result += "IX"
        if num >= 5:
            num = num - 5
            result += "V"
        if num >= 4:
            num = num - 4
            result += "IV"
        while num >= 1:
            num = num - 1
            result += "I"

        return result


s3 = Solution3()
print(s3.intToRoman(431))
