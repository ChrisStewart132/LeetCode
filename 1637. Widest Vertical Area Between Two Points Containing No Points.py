'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
'''
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_points = sorted(points, key=lambda x:x[0])

        gap = abs(sorted_points[0][0] - sorted_points[1][0])
        for i in range(2, len(sorted_points)):
            print(gap)
            temp = sorted_points[i][0] - sorted_points[i-1][0]
            if gap < temp:
                gap = temp

        return gap