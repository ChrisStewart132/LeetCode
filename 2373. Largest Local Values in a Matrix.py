'''
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

    maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
'''
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        output = [[0]*(len(grid)-2) for i in range(len(grid)-2)]
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid)-1):
                n = grid[i][j]
                for y in range(-1, 2):
                    for x in range(-1,2):
                        n = max(n, grid[i+y][j+x])
                output[i-1][j-1] = n

        return output