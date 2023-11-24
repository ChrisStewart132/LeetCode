'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root, isLeft=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == root.right == None:
            return root.val if isLeft else 0
        total = 0
        if root.left:
            total += self.sumOfLeftLeaves(root.left, True)
        if root.right:
            total += self.sumOfLeftLeaves(root.right, False)
        return total
        
