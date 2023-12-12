'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
'''
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i, n = 0, len(arr)//4
        while i < len(arr):
            if arr[i] == arr[i+n]:
                return arr[i]
            i = arr.index(arr[i+n])
        return 0