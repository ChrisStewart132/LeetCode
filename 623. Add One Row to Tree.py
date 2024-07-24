'''
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _insert_child(self, parent, val):
        parent.left = TreeNode(val, parent.left, None)
        parent.right = TreeNode(val, None, parent.right)
    def addOneRow(self, root, val, depth, d=1):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if root is None:
            return
        if depth == 1:
            return TreeNode(val, root, None)

        if d+1 == depth:
            self._insert_child(root, val)
        else:
            self.addOneRow(root.left, val, depth, d+1)
            self.addOneRow(root.right, val, depth, d+1)
        return root