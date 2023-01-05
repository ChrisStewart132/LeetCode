'''
here are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
'''
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0

        # sort points by (start, end)
        sorted_points = sorted(points, key=lambda p: (p[1], p[0]) )

        # iterate through sorted_points shooting an arrow to hit all previous baloons
        x_end = None
        i = 0
        while i < len(sorted_points):
            current = sorted_points[i]
            if x_end == None:
                x_end = current[1]
            elif current[0] > x_end:# shoot arrow
                #print("shoot", current)
                total += 1
                x_end = current[1]
                           
            i += 1


        return total if x_end == None else total + 1