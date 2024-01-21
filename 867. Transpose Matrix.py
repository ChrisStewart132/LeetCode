'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        output = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[j][i] = matrix[i][j]
        return output

