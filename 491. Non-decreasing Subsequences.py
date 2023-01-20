'''
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
'''
class Solution(object):
    def _findSubsequences(self, nums, cache):
        candidates = []
        for i in range(len(nums)):         
            candidate = tuple(nums[:i] + nums[i+1:])
            if len(candidate) > 1 and candidate not in cache:
                candidates.append(candidate)             
                cache[candidate] = self._findSubsequences(candidate, cache)
                candidates += cache[candidate]

        return candidates

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # generate all unique subsequences using a cache, enforce order
        candidates = self._findSubsequences(nums, {}) + [tuple(nums)] if len(nums) > 1 else []
        return [x for x in candidates if list(x) == sorted(x)]



            