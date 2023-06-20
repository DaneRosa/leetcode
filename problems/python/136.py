'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 


'''

""" Here is the explanation for the code above:
1. XOR of a number with itself is 0.
2. XOR of a number with 0 is the number itself.
So if we XOR all numbers together, it would effectively cancel out all elements that appears twice leaving us with only the element that appears once.
"""
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums, 0)