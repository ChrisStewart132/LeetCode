'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution(object):
    def removeElement(self, nums, val, i=0, offset=0):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if i == len(nums):
            return offset
        if nums[i] != val:
            nums[i-offset] = nums[i]
        elif nums[i] == val:
            offset += 1

            
        # get offset of last call
        offset = self.removeElement(nums, val, i+1, offset)
        
        if i == 0:# first call
            return len(nums) - offset
        else:
            return offset
        
        
        
        