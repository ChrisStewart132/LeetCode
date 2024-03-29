'''
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

    i < j < k,
    nums[j] - nums[i] == diff, and
    nums[k] - nums[j] == diff.

Return the number of unique arithmetic triplets.
'''
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        s = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[j] - nums[i] == diff == nums[k] - nums[j]:
                        s.add((i,j,k))
        return len(s)