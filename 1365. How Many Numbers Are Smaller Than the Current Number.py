'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sorted(nums)# n log n
        d = {}
        prev, prev_i = s[0], 0
        for i in range(len(nums)):# n
            if s[i] != prev:
                d[prev] = prev_i      
                prev, prev_i = s[i], i
        d[prev] = prev_i
        d[s[0]] = 0
        return [d[k] for k in nums]# n