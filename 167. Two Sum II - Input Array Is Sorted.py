'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
class Solution(object):
    def search(self, arr, target, l, r):
        while l < r:
            i = (l + r) // 2
            if arr[i] == target:
                return i
            elif arr[i] < target:
                l = i + 1 
            else:
                r = i - 1
        return l if arr[l] == target else -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(numbers):
            r = self.search(numbers, target-num, i+1, len(numbers)-1)
            if r != -1:
                return [i+1, r+1]
