'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        #print(root.val)
        n = 0
        if low <= root.val <= high:
            n += root.val
        if root.val < high:
            n += self.rangeSumBST(root.right, low, high)
        if root.val > low:
            n += self.rangeSumBST(root.left, low, high)
        
        return n