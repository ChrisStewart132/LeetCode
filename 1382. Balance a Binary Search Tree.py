'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, root):
        if root == None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def arrToBST(self, arr, parent=None):
        if len(arr) == 0:
            return
        m = len(arr)/2
        root = TreeNode(arr[m])
        if parent:
            if root.val < parent.val:
                parent.left = root
            else:
                parent.right = root
        self.arrToBST(arr[:m], root)
        self.arrToBST(arr[m+1:], root)
        return root

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = self.inOrder(root)
        return self.arrToBST(arr)