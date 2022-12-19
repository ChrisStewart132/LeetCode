'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''
class Solution(object):
    def validPath(self, n, edges, source, destination, expanded=None, graph=None):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if expanded == None:
            expanded = [0 for x in range(n)]
            graph = {}
            for edge in edges:# create dictionary to prevent iterating entire graph each call
                if edge[0] in graph:
                    graph[edge[0]] += [edge[1]]
                else:
                    graph[edge[0]] = [edge[1]]

                if edge[1] in graph:
                    graph[edge[1]] += [edge[0]]
                else:
                    graph[edge[1]] = [edge[0]]

        # base case
        if source == destination or expanded[destination] == 1:
            expanded[destination] = 1
            return True

        if expanded[source] == 1:
            return False

        expanded[source] = 1

        # traverse from source to neighbours and re-curse
        for node in graph[source]:                   
            if self.validPath(n, edges, node, destination, expanded, graph):
                return True
    
        # no neighbours had a valid path so no path found
        return False


