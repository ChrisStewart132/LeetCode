'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''
class Solution(object):
    def allPathsSourceTarget(self, graph, n=0, path=None, output=None):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if path == None:
            path, output = [], []

        if n == len(graph)-1:
            output.append(path + [n])

        path += [n]
        for edge in graph[n]:
            _path = [x for x in path]
            self.allPathsSourceTarget(graph, edge, _path, output)

        return output