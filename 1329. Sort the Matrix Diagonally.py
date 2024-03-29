'''
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        n_diagonals = m + n - 1# 6 = 3m + 4n, 5 = 3m + 3n, 4 = 3m + 2n, 5 = 2m + 4n.....
        diagonals = [[] for i in range(n_diagonals)]
        
        for i in range(m):# row
            for j in range(n):# col
                diagonals[(i-j) % n_diagonals].append(mat[i][j])

        for i in range(n_diagonals):
            diagonals[i] = sorted(diagonals[i], reverse=True)

        output = [[0]*n for i in range(m)]
        for i in range(m):# row
            for j in range(n):# col               
                output[i][j] = diagonals[(i - j) % n_diagonals].pop()


        return output