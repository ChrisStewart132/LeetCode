'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #return sum([sum([1 for i in range(len(row)) if row[i] < 0]) for row in grid])
        total = 0
        for row in grid:
          if row[0] < 0:
            total += len(row)
          else:
            i = len(row)-1
            while i > -1 and row[i] < 0:
              total, i = total+1, i-1
        return total

        
        