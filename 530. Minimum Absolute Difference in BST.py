'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, root):
        if root == None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = self.inOrder(root)
        return min([abs(values[i-1] - values[i]) for i in range(1, len(values))])