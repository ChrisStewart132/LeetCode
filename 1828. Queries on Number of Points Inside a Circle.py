'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
'''
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = [0 for x in queries]
        for i, q in enumerate(queries):
            for j, p in enumerate(points):
                if (p[0] - q[0])**2 + (p[1] - q[1])**2 <= q[2]**2:
                    result[i] += 1
        return result