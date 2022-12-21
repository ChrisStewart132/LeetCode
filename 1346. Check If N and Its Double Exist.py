'''
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

'''
class Solution(object):
    def checkIfExist(self, arr, i=0, s=None):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if s == None:
            s = set()
            
        if i == len(arr):
            return False
        elif arr[i] % 2 == 0 and arr[i] / 2 in s or arr[i] * 2 in s:
            return True
        else:
            s.add(arr[i])
        
        return self.checkIfExist(arr, i+1, s)

        