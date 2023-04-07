# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root, parent=None, grandparent=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if parent == None:
            left = self.sumEvenGrandparent(root.left, root, None)
            right = self.sumEvenGrandparent(root.right, root, None)
        else:
            left = self.sumEvenGrandparent(root.left, root, parent)
            right = self.sumEvenGrandparent(root.right, root, parent)

        return root.val + left + right if grandparent and grandparent.val % 2 == 0 else left + right
