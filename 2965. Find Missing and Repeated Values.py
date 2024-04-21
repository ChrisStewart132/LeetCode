'''
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
'''
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        cache = [0 for i in range(n**2+1)]
        output = [0,0]
        for i in range(n):
            for j in range(n):
                cache[grid[i][j]] += 1
                if cache[grid[i][j]] > 1:
                    output[0] = grid[i][j]  
        for i in range(1, len(cache)):
            if cache[i] == 0:
                output[1] = i
                break
        
        return output
                    