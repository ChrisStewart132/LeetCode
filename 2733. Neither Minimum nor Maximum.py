'''
Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.
'''
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1

        mx, mn = max(nums), min(nums)
        for i in range(len(nums)):
            if mn < nums[i] < mx:
                return nums[i]           
        return -1
