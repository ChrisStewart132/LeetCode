'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

'''
class Solution(object):
    def _increasing(self, arr, i=1):
        if i == len(arr):
            return i-1      
        elif arr[i] > arr[i-1]:
            return self._increasing(arr,i+1)
        else:
            return i# index where arr did not increase
        
    def _decreasing(self, arr, i=None):
        if i == None:
            i = len(arr)-2
            
        if i == -1:
            return 0      
        elif arr[i] > arr[i+1]:
            return self._decreasing(arr,i-1)
        else:
            return i# index where arr did not decrease
        
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        i,d = self._increasing(arr), self._decreasing(arr)
        print(i,d)
        return i == d+2