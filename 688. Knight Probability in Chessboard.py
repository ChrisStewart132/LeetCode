'''
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.
'''

class Solution(object):
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    #results = []
    cache = {}# dp
    def knightProbability(self, n, k, row, column, depth=0):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        if depth == 0:# reset cache between problems
            self.cache.clear()

        if (k, row, column) in self.cache:
            return self.cache[(k, row, column)]

        # knight still on board
        if 0 <= row < n and 0 <= column < n:
            
            # knight succesfully moved
            if k == 0:
                #self.results.append((row,column))
                return 1

            p = 0.0
            for y, x in self.moves:# for each possible move
                p += self.knightProbability(n, k-1, row+y, column+x, depth+1)
            
            #print(p,k,8**k, p/(8**k), depth, self.results)
            self.cache[(k, row, column)] = p
            return p if depth > 0 else p/(8**k)
        else:# knight out of bounds
            return 0
