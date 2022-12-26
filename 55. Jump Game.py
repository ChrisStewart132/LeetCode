'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''
class Solution(object):
    def canJump(self, nums, i=0, cache=None):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if cache == None:
            cache = {}

        if i >= len(nums) - 1:
            return True

        for j in range(nums[i], 0, -1):
            result = cache[i+j] if i+j in cache else self.canJump(nums, i+j, cache)
            cache[i+j] = result
            if result:
                return True







