'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root, val=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if val == None:
            val = root.val
        return root.val == val and self.isUnivalTree(root.left, val) and self.isUnivalTree(root.right, val)
        