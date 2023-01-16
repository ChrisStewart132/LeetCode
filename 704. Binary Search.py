'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution(object):
    def _search(self, nums, target, l, r):
        m = l + (r-l) // 2
        if nums[m] == target:
            return m
        elif l >= r:
            return -1
        elif nums[m] < target:
            return self._search(nums, target, m+1, r)
        else:
            return self._search(nums, target, l, m)
            
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._search(nums, target, 0, len(nums)-1)
        
        