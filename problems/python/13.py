'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

IV
IX
XL
XC
CD
CM

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }
        # maps each Roman numeral to its corresponding integer value

        skip_next_n = False
        int_sum = 0
        for idx, n in enumerate(s):
            # iterates through each character in the input string
            if skip_next_n == True:
                # If "skip_next_n" is True, the loop skips the current iteration without executing any code.
                skip_next_n = False
                continue
            try:
                # If the current character is a valid Roman numeral, the code checks whether the value of the current numeral is less than the value of the next numeral
                if roman_dic[n] < roman_dic[s[idx + 1]]:
                # If the value of the current numeral is less than the value of the next numeral
                    int_sum +=  roman_dic[s[idx + 1]] - roman_dic[n]
                    # adds the value of the current numeral to the integer sum
                    skip_next_n = True
                    # skips to prevent double accounts
                    continue
                else:
                    int_sum += roman_dic[n]
                    # If it is not, the code adds the value of the current numeral to "int_sum"
            except:
                int_sum += roman_dic[n]
                
        return int_sum