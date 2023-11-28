'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target. 
'''
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        for j in range(len(nums)):# j < n
            for i in range(j):# 0 <= i < j
                if nums[i] + nums[j] < target:
                    result += 1
        return result
        