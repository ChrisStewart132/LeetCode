# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def _minDepth(self, root):
        if root.left == root.right == None:
            return 1
        left = self.minDepth(root.left) if root.left else 10**5
        right = self.minDepth(root.right) if root.right else 10**5
        return 1 + min(left, right)

    def minDepth(self, root):
        return 0 if root == None else self._minDepth(root)

        
        

