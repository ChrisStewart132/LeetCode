'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def _leafNodes(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        return [] + self._leafNodes(root.left) + self._leafNodes(root.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = self._leafNodes(root1)
        leaf2 = self._leafNodes(root2)
        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True


        