'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution(object):
    # Python 2
    def romanToIntMarwan(self, s):
        """
        :type s: str
        :rtype: int
        """
        upcase_roman = s.upper()
        normal_numbers = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        weird_numbers = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "III": 3,
            "II": 2
        }
        total_value = 0
        for roman_number, value in weird_numbers.iteritems():
            while roman_number in s:
                s = s.replace(roman_number, "", 1)
                total_value += value
        for roman_number, value in normal_numbers.iteritems():
            while roman_number in s:
                s = s.replace(roman_number, "", 1)
                total_value += value
        return total_value    

    # fast as fuck
    def romanToInt(self, s: str) -> int:
        romDic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        prevVal = 0
        for i, char in enumerate(s):
            curVal = romDic[char]
            if i == 0 or curVal <= prevVal:
                result += curVal
            elif curVal > prevVal:
                # need to reduce 2 times, because it has been added previously
                result = result - 2 * prevVal + curVal
            prevVal = curVal
        
        return result