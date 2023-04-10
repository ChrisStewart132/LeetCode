# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target, init=True):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root == None:
            return
        left = self.removeLeafNodes(root.left, target, False)
        right = self.removeLeafNodes(root.right, target, False)
        if left == 1:
            root.left = None
        if right == 1:
            root.right = None
        if root.left == root.right == None and root.val == target:# leaf
            return None if init else 1# delete the connection between this node and its parent
        return root
            
