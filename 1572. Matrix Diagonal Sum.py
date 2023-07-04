'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        output = 0
        for i in range(len(mat)):
            output += mat[i][i]
            if i != len(mat)-1-i:
                output += mat[i][len(mat)-1-i]
        return output