'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''
class Solution(object):
    cache = {}
    def minFallingPathSum(self, matrix, i=0, j=0, depth=None):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # init, call on entire top row (self, + other top row start positions)
        if depth == None:
            self.cache = {}
            solutions = []
            for k in range(0, len(matrix)):
                solutions += [self.minFallingPathSum(matrix, 0, k, 0)]
            return min(solutions)

        # reached bottom of matrix
        if i == len(matrix):
            return 0 

        current = matrix[i][j]
        left, right, down = 10**9, 10**9, 10**9 # prevents considering paths that couldn't traverse for a min solution
        # traverse down if possible         
        if i < len(matrix):
            if j > 0:
                left = self.cache[(i+1,j-1)] if (i+1,j-1) in self.cache else self.minFallingPathSum(matrix, i+1, j-1, depth+1)
                self.cache[(i+1,j-1)] = left
            if j+1 < len(matrix[i]):

                right = self.cache[(i+1,j+1)] if (i+1,j+1) in self.cache else self.minFallingPathSum(matrix, i+1, j+1, depth+1)
                self.cache[(i+1,j+1)] = right

            down = self.cache[(i+1,j)] if (i+1,j) in self.cache else self.minFallingPathSum(matrix, i+1, j, depth+1) 
            self.cache[(i+1,j)] = down          


        return min(current + left, current + right, current + down)