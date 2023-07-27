'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {nums[0]:1}
        majority_element = nums[0]
        n = len(nums)//2
        for i in range(1, len(nums)):
            cache[nums[i]] = cache[nums[i]] + 1 if nums[i] in cache else 1
            if cache[nums[i]] > cache[majority_element]:
                majority_element = nums[i] 
            if cache[majority_element] > n:
                break
        
        return majority_element
