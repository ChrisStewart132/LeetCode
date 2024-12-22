'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = -1
        for i in range(len(nums)):
            l = min(nums[:i+1])
            r = max(nums[i+1:] + [l])
            if r > l:
                output = max(output, r-l)
        return output


        