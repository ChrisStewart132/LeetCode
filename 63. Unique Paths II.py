'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        cache = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:# goal or start blocked by obstacle
            return 0
        def _uniquePathsWithObstacles(m, n):
            if (m,n) in cache:# dp
                return cache[(m,n)]
            elif m == 1 == n:# success
                return 1
            elif m == 0 or n == 0 or obstacleGrid[m-1][n-1] == 1:# out of bounds or obstacle
                return 0
            cache[(m-1,n)] = _uniquePathsWithObstacles(m-1, n)
            cache[(m,n-1)] = _uniquePathsWithObstacles(m, n-1)
            return cache[(m-1,n)] + cache[(m,n-1)]
        return _uniquePathsWithObstacles(m, n)