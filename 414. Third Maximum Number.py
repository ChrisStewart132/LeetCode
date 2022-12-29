'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        ordered_nums_set = sorted(list(nums_set), key=lambda x:x)
        
        if len(ordered_nums_set) < 3:
            return ordered_nums_set[-1]
        else:
            return ordered_nums_set[-3]
        