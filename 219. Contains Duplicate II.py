'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and i not in cache[num]:
                cache[num].append(i)
            else:
                cache[num] = [i]

        for num in cache.keys():
            for i in cache[num]:
                for j in cache[num]:
                    if i != j and abs(i-j) <= k:
                        return True
        
        return False