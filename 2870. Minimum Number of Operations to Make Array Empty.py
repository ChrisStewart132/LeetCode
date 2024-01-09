'''
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

    Choose two elements with equal values and delete them from the array.
    Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
'''
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            try:
                d[num] += 1
            except KeyError:
                d[num] = 1
        
        output = 0
        for k,v in d.items():
            if d[k] < 2:
                return -1
            while d[k] > 0 and d[k] % 3 != 0:
                output += 1
                d[k] -= 2
            output += d[k]/3
        return output