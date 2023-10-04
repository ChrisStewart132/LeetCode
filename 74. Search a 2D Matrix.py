'''
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            middle = (l+r)//2
            i,j = middle // n, middle % n# convert 1d to 2d indices
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = middle+1
            else:
                r = middle-1

        return False