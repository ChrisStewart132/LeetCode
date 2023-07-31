'''
You are given a positive integer array nums.

    The element sum is the sum of all the elements in nums.
    The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.

Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
'''
class Solution(object):
    def digitSum(self, num):
        n = 0
        while num >= 10:
            n += num%10
            num -= num%10
            num /= 10
        return n + num

    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return abs(sum(nums) - sum([self.digitSum(num) for num in nums]))

