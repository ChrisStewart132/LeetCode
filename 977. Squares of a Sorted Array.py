'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
class Solution(object):
    def sortedSquares(self, nums, l=0, r=None):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if r == None:
            r = len(nums)-1
            
        if l == r:            
            return [nums[r]**2]
        elif abs(nums[l]) > abs(nums[r]):
            return self.sortedSquares(nums, l+1, r) + [nums[l]**2]
        else:
            return self.sortedSquares(nums, l, r-1) + [nums[r]**2]
            