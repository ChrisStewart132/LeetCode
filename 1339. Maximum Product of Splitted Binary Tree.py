'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cache = {}
    def treeSum(self, root):
        if root == None:
            return 0

        if root.left in self.cache:
            left = self.cache[root.left]
        else:
            left = self.treeSum(root.left)
            self.cache[root.left] = left

        if root.right in self.cache:
            right = self.cache[root.right]
        else:
            right = self.treeSum(root.right)
            self.cache[root.right] = right

        return root.val + left + right

    def maxProduct(self, root, total=None):
        # have to reduce modulo x after finding max 
        return self._maxProduct(root) % ((10**9)+7)

    def _maxProduct(self, root, total=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if total==None:
            total = self.treeSum(root)
        if root == None:
            return 0
        left = self.treeSum(root.left)
        right = self.treeSum(root.right)
        break_left = left * (total-left)
        break_right = right * (total-right)
        return max(break_left,break_right,self._maxProduct(root.left, total),self._maxProduct(root.right, total))