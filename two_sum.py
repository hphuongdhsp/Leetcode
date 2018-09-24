"""
problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example: 

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        # We will use the Hash Table to solve this problem
        # make sure that the nums is good dimension. It means len(nums)>=2
        if len(nums) <= 1:
            return False
        table = {} # define the Hash table
        for i in range(len(nums)):
            if nums[i] in table:
                return [table[nums[i]], i]
            else:
                table[target - nums[i]] = i
        # We also use the Brute Force to solve this problem. For this algorithm, it costs O(n^2), because of using 2 for loop. 
