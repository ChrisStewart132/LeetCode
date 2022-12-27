'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''
class Solution(object):
    def sortArrayByParity(self, nums,l=0,r=None):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if r == None:
            r = len(nums)-1
            
        # move l to point to first odd number
        while l < len(nums) and nums[l] % 2 == 0:
            l += 1
            
        # move r to point to first even number from the right of the list
        while r > 0 and nums[r] % 2 == 1:
            r -= 1
            
        if l >= r:# finished
            return nums
        else:# swap l and r
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            
        return self.sortArrayByParity(nums,l,r)