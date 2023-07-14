'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
'''
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min(nums)
        i = nums.index(min1)
        min2 = min(nums[:i] + nums[i+1:])

        max1 = max(nums)
        i = nums.index(max1)
        max2 = max(nums[:i] + nums[i+1:])

        return max1 * max2 - min1 * min2