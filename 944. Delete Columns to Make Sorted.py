'''
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
'''
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        result = 0
        
        for i in range(len(strs[0])):# column index
            for j in range(len(strs)):# row index
                if j == 0:
                    prev = ord(strs[j][i])
                    continue    

                current = ord(strs[j][i])
                
                if current < prev:
                    result += 1
                    break

                prev = current

        return result