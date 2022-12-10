'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''
class Solution(object):
    def findNumbers(self, nums, i=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if i == len(nums):
            return 0
        
        n_digits = 0
        while nums[i] >= 1:
            nums[i] /= 10
            n_digits += 1
        #print(nums[i], n_digits)
        
        if n_digits % 2 == 0:
            return 1 + self.findNumbers(nums, i+1)
        else:
            return 0 + self.findNumbers(nums, i+1)