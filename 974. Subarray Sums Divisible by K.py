'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
'''
class Solution(object):
    def _subarraysDivByK(self, nums, k, n, cache, l, r):
        if l == r:
            return 1 if nums[r] % k == 0 else 0
        elif (cache[r] - cache[l-1]) % k == 0:
            n += 1
        
        for i in range(2):
            # create sub-array by moving first or last element indices
            key = (l, r-1) if i == 0 else (l+1, r)

            if key not in cache:# prune calculated sub_array's 
                cache[key] = self._subarraysDivByK(nums, k, 0, cache, key[0], key[1])
                n += cache[key]

        return n

    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cache = {}# stores n of each sub-array (l,r) and sum of each left sub-array (r)
        cache[-1] = 0
        cache[0] = nums[0] % k     
        for i in range(1, len(nums)):
            cache[i] = cache[i-1] + (nums[i] % k)

        return self._subarraysDivByK(nums, k, 0, cache, 0, len(nums)-1)      