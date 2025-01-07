"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
"""
class Solution(object):
    def inBounds(self, grid, i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

    def isSubIsland(self, grid1, grid2, i, j):
        if not (self.inBounds(grid1, i, j) and self.inBounds(grid2, i, j)):
            return True
        if grid2[i][j] == 0:
            return True
        test = grid1[i][j] == grid2[i][j] and grid1[i][j] == 1
        grid2[i][j] = 0
        neighbours = [
            self.isSubIsland(grid1,grid2,i,j+1),
            self.isSubIsland(grid1,grid2,i,j-1),
            self.isSubIsland(grid1,grid2,i+1,j),
            self.isSubIsland(grid1,grid2,i-1,j)
            ]
        return test and all(neighbours)
        
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and self.isSubIsland(grid1, grid2, i, j):
                    count += 1
        return count
        