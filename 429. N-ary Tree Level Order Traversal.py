'''
Given an n-ary tree, return the level order traversal of its nodes' values.

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
    def levelOrder(self, root, depth=0, output=None):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return

        if depth==0:
            output=[[]]
        if len(output) <= depth:
            output.append([])

        output[depth].append(root.val)

        for child in root.children:
            self.levelOrder(child, depth+1, output)

        return output