'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
ex:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={} 
        # Create an empty dictionary to store the values and their indices.
        for i,n in enumerate(nums): 
            # Iterate over the list of nums using the enumerate function.
            if n in dict: 
                # If the current value is already in the dictionary, 
                # return the indices of the two values since they add up to target.
                return dict[n],i 
            else: 
                # If the current value is not in the dictionary, store the difference between the 
                # target and the current value with the current index as a key-value pair in the dictionary.
                dict[target-n]=i