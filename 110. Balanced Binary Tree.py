'''
Given a binary tree, determine if it is
height-balanced
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if root == None:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            
            return 1 + max(l, r)
        
        return depth(root) != -1
