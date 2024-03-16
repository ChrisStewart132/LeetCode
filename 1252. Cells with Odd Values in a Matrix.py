'''
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

    Increment all the cells on row ri.
    Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
'''
class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for j in range(n)] for i in range(m)]
        for r,c in indices:
            for j in range(n):
                matrix[r][j] += 1
            for i in range(m):
                matrix[i][c] += 1

        output = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2 == 1:
                    output += 1
                    
        return output