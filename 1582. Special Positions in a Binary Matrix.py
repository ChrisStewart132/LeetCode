'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
'''
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = [0]*len(mat), [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        total = 0
        for i in range(len(rows)):
            if rows[i] == 1 == cols[mat[i].index(1)]:
                total += 1
                
        return total