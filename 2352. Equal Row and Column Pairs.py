'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = 0
        cache = []
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(grid)):
                if i == 0:# cache the created columns
                    cache.append([grid[k][j] for k in range(len(grid))])
                if row == cache[j]:
                    n += 1
        return n

