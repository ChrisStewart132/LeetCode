'''
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k, s=None):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        if s == None:
            s = set()
        if k-root.val in s:
            return True
        s.add(root.val)
        return self.findTarget(root.left, k, s) or self.findTarget(root.right, k, s)

        
