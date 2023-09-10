'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cache = {}
        target = len(grid)-1, len(grid[0])-1
        def _minPathSum(i=0, j=0):
            if (i,j) in cache:# dp
                return cache[(i,j)]
            elif i == len(grid) or j == len(grid[0]):# out of bounds
                return 1000000000
            elif (i,j) == target:# target reached
                return grid[i][j]
            cache[(i,j)] = grid[i][j] + min(_minPathSum(i,j+1), _minPathSum(i+1,j))
            return cache[(i,j)]
        return _minPathSum()