'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1). 
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        i = nums.index(m1)
        m2 = max (nums[:i] + nums[i+1:])
        return (m1-1) * (m2-1)