'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k. 
'''
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        for j in range(len(nums)):
            for i in range(j):
                output += 1 if nums[i] == nums[j] and i*j % k == 0 else 0
        return output