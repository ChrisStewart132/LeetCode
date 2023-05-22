'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    parent = None
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return

        head = self.increasingBST(root.left)
        
        if head == None:
            head = root
        if self.parent:
            self.parent.right = root
        else:
            head = root
        self.parent = root
        root.left = None

        self.increasingBST(root.right)
        return head
        