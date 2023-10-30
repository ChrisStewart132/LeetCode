'''
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

    For example, flipping [1,1,0] horizontally results in [0,1,1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

    For example, inverting [0,1,1] results in [1,0,0].

'''
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for i in range(n):# row
            for j in range(n//2):# col
                image[i][j], image[i][n-1-j] = abs(image[i][n-1-j] - 1), abs(image[i][j] - 1)
            if n % 2 == 1:# invert middle elements if n odd
                image[i][n//2] = abs(image[i][n//2] - 1)
        return image