'''
You are given an m x n integer array grid where grid[i][j] could be:

    1 representing the starting square. There is exactly one starting square.
    2 representing the ending square. There is exactly one ending square.
    0 representing empty squares we can walk over.
    -1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
'''
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cache = {}# dp
        directions = ((1,0), (0,1), (-1,0), (0,-1))
        m, n = len(grid), len(grid[0])
        y, x = None, None# starting pos
        for i in range(m):
            if 1 in grid[i]:
                y, x = i, grid[i].index(1)

        target_len = m*n - sum([grid[i].count(-1) for i in range(m)])# how long a succesful unique path will be
        target_len -= 1# 1 subtracted as paths dont include current pos when checking success

        def _uniquePathsIII(y, x, path):
            key = (p for p in path)
            if key in cache:
                return cache[key]
            if not(-1 < y < m) or not(-1 < x < n):# out of bounds
                return 0
            if grid[y][x] == -1 or (y, x) in path:# obstacle or path must visit each point once
                return 0
            if grid[y][x] == 2 and len(path) == target_len:# successfully reached each pos once
                return 1
     
            total = 0
            path += [(y, x)]
            for dy, dx in directions:
                total += _uniquePathsIII(y+dy, x+dx, path)
            path.pop()

            cache[key] = total
            return total

        return _uniquePathsIII(y, x, [])
            
