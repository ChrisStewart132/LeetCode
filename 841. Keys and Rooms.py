'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
'''
class Solution(object):
    def canVisitAllRooms(self, rooms, i=0, visited=None):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if visited == None:
            visited = [0 for x in rooms]

        if visited[i] == 1:
            return           
        visited[i] = 1
        
        for key in rooms[i]:
            self.canVisitAllRooms(rooms, key, visited)


        if i == 0:
            return all(visited)