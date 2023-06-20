'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"

'''
# alphabet
# a-z = 26
# Python ord() and chr() functions are exactly opposite of each other.
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Create an empty string for storing the characters...
        output = ""
        # Run a while loop while columnNumber is positive...
        while columnNumber > 0:
            # Subtract 1 from columnNumber because index starts at 0 and get current character by doing modulo of columnNumber by 26 for the alphabet
            output = chr(
                # chr gets char from unicode
                ord('A') + (columnNumber - 1) % 26
                # ord gets unicode
                ) + output
            # Divide columnNumber by 26 to get what is left
            columnNumber = (columnNumber - 1) // 26
        # Return the output string.
        return output