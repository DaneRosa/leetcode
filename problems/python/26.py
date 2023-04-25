'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        # use a set to get the unique values
        dedup = set(nums)
        # get the number of unique values
        dedup_len = len(dedup)
        # sort the unique values and convert it to a list
        dedup = sorted(dedup)
        k = dedup_len # the number of unique values is the length of dedup
        # replace the first k elements of nums with the unique values
        nums[:k] = dedup
        return k
