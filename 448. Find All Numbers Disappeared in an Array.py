'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set([x for x in nums])
        output = []
        for i in range(1, len(nums)+1, 1):
            if i not in s:
                output.append(i)
            if len(nums) == len(output) + len(s):
                break

        return output
            