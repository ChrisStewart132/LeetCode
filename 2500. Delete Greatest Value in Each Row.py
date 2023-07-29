'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

    Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
    Add the maximum of deleted elements to the answer.

Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''
class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        for n in range(len(grid[0])):# col
            ms = [max(grid[m]) for m in range(len(grid))]
            output += max(ms)
            for m in range(len(grid)):# row
                grid[m].remove(ms[m])



        return output