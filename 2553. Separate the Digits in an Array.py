'''
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

    For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

'''
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums:
            s = []
            while num > 0:
                s.append(num % 10)
                num -= num%10
                num /= 10
            while len(s) > 0:
                output.append(s.pop())
        return output