'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root, depth=0):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return depth 
        return max([self.maxDepth(child, depth+1) for child in root.children]+[depth+1])

