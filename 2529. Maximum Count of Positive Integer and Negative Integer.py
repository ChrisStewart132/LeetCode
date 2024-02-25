'''
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
'''
class Solution(object):
    def searchLeft(self, nums, target=0):
        l, r = 0, len(nums)-1
        while l+1 < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m
            else:
                r = m-1
        if l+1 < len(nums) and nums[l+1] < target:
            return l+1
        return l if nums[l] < target else -1

    def searchRight(self, nums, target=0):
        l, r = 0, len(nums)-1
        while l+1 < r:
            m = (l+r)//2
            if nums[m] > target:
                r = m
            else:
                l = m+1
        if nums[l] > target:
            return l
        elif l+1 < len(nums) and nums[l+1] > target:
            return l+1
        return -1

    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the index a of [..a,b,..] where a < 0 and b > 0  
        neg = self.searchLeft(nums)
        pos = self.searchRight(nums)
        neg_count = neg+1
        pos_count = len(nums) - pos if pos > -1 else 0
        #print(neg, pos, nums[neg], nums[pos])
        #print(neg_count, pos_count, len(nums))
        return max(neg_count, pos_count)