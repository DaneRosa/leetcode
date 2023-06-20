'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 
'''

title = "A"

# return column num
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # chr() give char
        # ord() gives num
        # % 26 mod 26 means % then remainder
        # 'A' still not sure why we start at A 
        # // 26 divide by 26 to get val
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            # for each letter in column title
            digit = ord(letter)-64
            # By subtracting the code by 64, we can map letters to the numbers from 1 to 26.
            ans += digit * 26**pos
            pos += 1
            
        return ans
