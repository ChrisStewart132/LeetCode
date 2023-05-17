'''
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root, n=''):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left == root.right == None:
            return int(n+str(root.val), 2)

        return self.sumRootToLeaf(root.left, n + str(root.val)) + self.sumRootToLeaf(root.right, n + str(root.val))
        