# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if original == target:
            return cloned

        left, right = None, None
        if original.left:
            left = self.getTargetCopy(original.left, cloned.left, target)
        if original.right:
            right = self.getTargetCopy(original.right, cloned.right, target)

        if left:
            return left
        elif right:
            return right
        

