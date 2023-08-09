'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(l,r):
            if l == None == r:
                return True

            if l == None and r or r == None and l or l.val != r.val:
                return False

            return _isSymmetric(l.left, r.right) and _isSymmetric(l.right, r.left)

        return _isSymmetric(root.left, root.right) if root else True