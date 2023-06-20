'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''
class Solution(object):
    def runningSum(self, nums, s=0):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        s = s + nums[0]
        return [s] + self.runningSum(nums[1:], s)
