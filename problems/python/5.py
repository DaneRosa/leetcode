'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

inout s = 'asdkjfhsedfoooof'

'''

# return longest palindromatic substring
# use reverese
# sliding window
# check if matches first index

'''
check if 0 in string 
    if so grab the next index? 
    if so do the between values match
        do the between values match if reversed

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialize a string to store the longest palindrome
        sub = ''
        
        # loop through the input string
        for indi, i in enumerate(s):
            # loop through the input string again
            for indj, j in enumerate(s[indi:], start=indi):
                # check if the substring is a palindrome
                # s[starts at index i, ends at index j + 1] this is to expand the window
                # s[starts at index i, ends at index j + 1][::-1] this is to reverse the string
                # list[<start>:<stop>:<step>]
                if i == j and s[indi:indj+1] == s[indi:indj+1][::-1]:
                    # update the longest palindrome
                    if len(s[indi:indj+1]) > len(sub):
                        sub = s[indi:indj+1]
        return sub
    
Solution.longestPalindrome(self=Solution, s='babad')