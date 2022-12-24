'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''
class Solution(object):
    def replaceElements(self, arr, i=None, x=None):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if i == None:
            self.replaceElements(arr, len(arr)-2, arr[-1])
            arr[-1] = -1
            return arr
                
        if i < 0:
            return 
        temp = x
        if arr[i] > x:
            x = arr[i]
        arr[i] = temp
        self.replaceElements(arr, i-1, x)
        

            
        
        
        
        
        
    
        