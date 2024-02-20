'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isValidBST(root, mn, mx):
            if root == None:
                return True
            if not(mn < root.val < mx):
                return False
            return _isValidBST(root.left, mn, root.val) and _isValidBST(root.right, root.val, mx)

        return _isValidBST(root.left, -2**31-1, root.val) and _isValidBST(root.right, root.val, 2**31)

        

        