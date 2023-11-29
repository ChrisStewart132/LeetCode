'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #return sum([min(nums[i], nums[i+1]) for i in range(0, len(nums), 2)])
        output = 0
        for i in range(0, len(nums), 2):
            output += min(nums[i], nums[i+1])
        return output