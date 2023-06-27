'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        for n in nums:
            cache[n] = cache[n] + 1 if n in cache else 1
        return sum([(cache[k]*(cache[k]-1))//2 for k in cache.keys()])