'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _pruneTree(self, root):
        if root is None:
            return False
        left = self._pruneTree(root.left)
        right = self._pruneTree(root.right)
        # prune child trees
        if not left:
            root.left = None
        if not right:
            root.right = None
        # return tree.contains(1)
        return root.val == 1 or left or right

    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        rootContainsOne = self._pruneTree(root)
        return root if rootContainsOne else None