'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums, i=0, total=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if i >= len(nums):
            return 0
        
        while i < len(nums) and nums[i] == 1:
            total+=1
            i+=1
            
        return max(total, self.findMaxConsecutiveOnes(nums, i+1, 0))

            