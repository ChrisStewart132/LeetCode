'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = {}
        def _uniquePaths(m, n):
            if (m,n) in cache:
                return cache[(m,n)]
            if m == 1 == n:# success
                return 1
            elif m == 0 or n == 0:# out of bounds
                return 0
            cache[(m-1,n)] = _uniquePaths(m-1, n)
            cache[(m,n-1)] = _uniquePaths(m, n-1)
            return cache[(m-1,n)] + cache[(m,n-1)]
        return _uniquePaths(m, n)