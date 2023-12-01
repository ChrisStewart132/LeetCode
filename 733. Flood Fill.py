'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
'''
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        frontier = set()# contains positions recoloured
        stack = [(sr, sc)]
        old_color = image[sr][sc]
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        while len(stack) > 0:
            y, x = stack.pop()
            if image[y][x] != old_color:
                continue
            image[y][x] = color
            frontier.add((y,x))
            for dy, dx in directions:
                pos = (y+dy,x+dx)
                if pos not in frontier and -1 < pos[0] < len(image) and -1 < pos[1] < len(image[0]):
                    stack.append(pos)
        return image