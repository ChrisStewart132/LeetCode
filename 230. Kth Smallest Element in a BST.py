'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        output = []
        def _kthSmallest(root):
            if root == None:
                return 
            if len(output) < k:
                _kthSmallest(root.left)
            if len(output) < k:
                output.append(root.val)
                _kthSmallest(root.right)    

        _kthSmallest(root)
        return output[-1]