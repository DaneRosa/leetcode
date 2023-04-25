'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # zip() function to iterate simultaneously over the same index of each string
        for a in zip(*strs):
            if len(set(a)) == 1: 
                ans += a[0]
            else: 
                return ans
        return ans


