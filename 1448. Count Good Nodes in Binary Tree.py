# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root, highest=-10**5):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        highest = max(highest, root.val)
        left = self.goodNodes(root.left, highest)
        right = self.goodNodes(root.right, highest)
        return 1 + left + right if root.val >= highest else left + right

        
