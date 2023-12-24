'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
'''
class Solution(object):
    directions = {"N":(0,1), "S":(0,-1), "E":(1,0), "W":(-1,0)}
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        pos = (0,0)
        s = set([pos])
        for char in path:
            pos = pos[0] + self.directions[char][0], pos[1] + self.directions[char][1]
            if pos in s:
                return True
            s.add(pos)
        return False
            

        