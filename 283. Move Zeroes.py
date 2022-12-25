'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
class Solution(object):
    def moveZeroes(self, nums, l=0,r=0):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if r >= len(nums):
            return nums
        
        # move l to the next zero
        while l < len(nums) and nums[l] != 0:
            l += 1
        r=l+1
        # move r to the next num following a zero
        while r < len(nums) and nums[r] == 0:
            r += 1


        if r >= len(nums) or l >= len(nums):
            return nums
        else:
            if r > l:
                nums[l] = nums[r]
                nums[r] = 0
            return self.moveZeroes(nums, l+1, r)