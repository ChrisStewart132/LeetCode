'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
 Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        count = {}
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        output = []
        for num in arr2:
            output += [num]*count[num]
        s2 = set(arr2)
        tail = []
        for num in arr1:
            if num not in s2:
                tail.append(num)

        return output + sorted(tail)