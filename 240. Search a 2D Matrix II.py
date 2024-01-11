'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        y,x = 0, len(matrix[0])-1
        
        def _searchMatrix(matrix, target, y, x):
            if y == len(matrix)-1:# search bottom row
                return target in matrix[y]
            elif x == 0:# search left col
                return target in [matrix[i][x] for i in range(y, len(matrix))]
            elif target == matrix[y][x]:
                return True
            elif target < matrix[y][x]:
                return _searchMatrix(matrix, target, y, x-1)
            else:
                return _searchMatrix(matrix, target, y+1, x)
            
        return _searchMatrix(matrix, target, y, x)
            
        
        