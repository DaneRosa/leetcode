'''
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

# int array 
# remove all vals = val 
# no order

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # track the number of elements in the array that are not equal to val.
        k = 0
        # For each element, we check whether it is equal to val
        for i in range(len(nums)):
            # If it is not equal to val, we copy it to the position k in the array and increment k.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
