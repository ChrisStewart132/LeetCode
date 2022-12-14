'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution(object):
    def rob(self, nums, i=0, cache=None):
        """
        :type nums: List[int]
        :rtype: int
        """
        if cache == None:
            cache = {}

        if i >= len(nums):
            return 0

        dont_rob = cache[i+1] if i+1 in cache else self.rob(nums, i+1, cache)
        cache[i+1] = dont_rob

        rob = cache[i+2] if i+2 in cache else self.rob(nums, i+2, cache)
        cache[i+2] = rob

        return max(dont_rob, rob+nums[i])