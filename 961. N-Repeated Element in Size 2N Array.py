'''
You are given an integer array nums with the following properties:

    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.

Return the element that is repeated n times.
'''
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(nums)//2):# search from both ends inwards
            if nums[i] in s:
                return nums[i]
            s.add(nums[i])
            if nums[-i-1] in s:
                return nums[-i-1]
            s.add(nums[-i-1])
