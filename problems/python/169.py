'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


input = [6,6,6,7,7]
6:3
7:2
'''
# create a dict of elm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # base case: 
        if len(nums) <= 1:
            # may want to return max(nums) for better handling
            return nums[0]
        max_val = 2
        max_key = 0
        dummy = {}
        for i in sorted(nums):
            if i in dummy: 
                dummy[i] +=1
            else:
                dummy[i] = 1
        for k,v in dummy.items:
            if v >= max_val:
                max_val = v
                max_key = k
        return max_key
                