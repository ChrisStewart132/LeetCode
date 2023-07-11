'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()# all nums
        s2 = set()# non-unique nums
        for num in nums:
            if num in s:
                s2.add(num)
            else:
                s.add(num)

        return sum(s-s2)
