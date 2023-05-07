'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 


'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert the binary strings to integers, add them, and convert back to binary
        # bin() returns a string containing a binary representation of a number.
        # int(a, base) converts the string a to an integer. base specifies the base in which string is if a is an integer.
        # [2:] removes the first two characters of a string. 
        # It is because bin() returns a string "0b10101", to remove "0b", we need to slice the string. """
        return bin(int(a, 2) + int(b, 2))[2:]