'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
''''
class Solution(object):
    def permute(self, nums, candidate=[]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(candidate) == len(nums):
            return [candidate]

        output = []
        for num in nums:
            if num not in candidate:
                child = [x for x in candidate] + [num]
                output += self.permute(nums, child)

        return output