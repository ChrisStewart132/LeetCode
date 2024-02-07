'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
'''
from math import floor

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        smooth_img = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                average, denominator = 0, 0
                for y in range(max(0,i-1), min(m,i+2)):
                    for x in range(max(0,j-1), min(n,j+2)):
                        try:
                            average += img[y][x]
                            denominator += 1
                        except IndexError:
                            pass
                smooth_img[i][j] = int(floor(average/denominator))
        return smooth_img
                
