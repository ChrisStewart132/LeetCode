'''
There are n teams numbered from 0 to n - 1 in a tournament.

Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and
 i != j team i is stronger than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament.
'''
class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i, team in enumerate(grid):
            if sum(team) == len(team)-1:
                return i
        return -1
        