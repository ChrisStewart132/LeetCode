# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2, root=None):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:# overlap
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            root = TreeNode(root1.val)
            root.left = self.mergeTrees(root1.left, root2)
            root.right = self.mergeTrees(root1.right, root2)
        elif root2:
            root = TreeNode(root2.val)
            root.left = self.mergeTrees(root1, root2.left)
            root.right = self.mergeTrees(root1, root2.right)
        
        return root
