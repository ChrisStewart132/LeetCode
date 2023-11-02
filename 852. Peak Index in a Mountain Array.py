'''
An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
'''
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l,r = 0, len(arr)-1
        while l < r:
            m = (l+r) // 2
            #peak = arr[m-1] > arr[m] < arr[m+1]
            increasing = arr[m-1] < arr[m] < arr[m+1]# l->m
            decreasing = arr[m-1] > arr[m] > arr[m+1]# r->m
            if increasing:
                l = m
            elif decreasing:
                r = m
            else:
                break
        return m