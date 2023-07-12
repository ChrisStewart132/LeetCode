'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
'''
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        cache = {}
        for edge in edges:   
            cache[edge[0]] = 1 if edge[0] not in cache else cache[edge[0]] + 1
            cache[edge[1]] = 1 if edge[1] not in cache else cache[edge[1]] + 1
            if cache[edge[0]] > 1:
                return edge[0]
            if cache[edge[1]] > 1:
                return edge[1]