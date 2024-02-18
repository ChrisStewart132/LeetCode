"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        pairs = [n for n in s if n > 0 and -n in s]
        return -1 if len(pairs) == 0 else max(pairs)
