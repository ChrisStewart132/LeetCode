'''
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''
class Solution(object):
    def search(self, arr, target):
        # search and return the closest value to target 
        l, r = 0, len(arr)-1
        while l+1 <= r:
            m = (l+r)//2
            if arr[m] < target:
                l = m+1
            else:
                r = m
        left = max(0, l-1)
        right = min(len(arr)-1, l+1)
        return min([abs(target-arr[i]) for i in range(left, right+1)])

    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        sorted2 = sorted(arr2)
        output = 0
        for num in arr1:
            dist = self.search(sorted2, num)
            if dist > d:
                output += 1
        return output
        