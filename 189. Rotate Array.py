'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # Store the last k elements in a temporary list
        temp = nums[n - k:]

        # Shift the first n-k elements to their new positions
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        # Place the stored k elements at the beginning of the list
        for i in range(k):
            nums[i] = temp[i]
