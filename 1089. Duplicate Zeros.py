'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
'''
class Solution(object):
    def duplicateZeros(self, arr, i=0):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        if i >= len(arr):
            return

        # move to zero index
        while i < len(arr) and arr[i] != 0:
            i += 1
        # i points to a zero
        
        # divide 
        self.duplicateZeros(arr, i+1)
        
        if i+1 < len(arr):
            # shift following elements from 0 right 1
            for j in range(len(arr)-1, i , -1):
                arr[j] = arr[j-1] # shift right

