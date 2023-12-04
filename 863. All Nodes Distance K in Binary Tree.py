'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # construct a graph / adjacency list of the tree
        # bfs search from the target node to a distance of k
            # return all nodes at distance k
        graph = {}
        def build_graph(curr, prev=None):
            if curr:
                l, r, c = curr.left, curr.right, curr.val
                if curr not in graph:
                    graph[c] = []
                if prev:
                    graph[c].append(prev.val)
                if l:
                    graph[c].append(l.val)
                    build_graph(l, curr)
                if r:
                    graph[c].append(r.val)
                    build_graph(r, curr)
                      
        build_graph(root)
        
        q, searched = [target.val], set()
        while k > 0 and len(q) > 0:
            # add all current nodes children to q
            n = len(q)
            for i in range(n):
                for neighbour in graph[q[i]]:
                    if neighbour not in searched:
                        q.append(neighbour)
                searched.add(q[i])# set the node as succesfully traversed/searched
            q = q[n:]# remove the parent nodes so the next depth nodes are contained in q
            k -= 1# decrement k as distance closes to 0

        return q# q contains the last depth nodes from the target node            
            