'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root, path=""):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if root.left == root.right == None:# leaf
            return [path + str(root.val)]

        left = self.binaryTreePaths(root.left, path + str(root.val) + "->")
        right = self.binaryTreePaths(root.right, path + str(root.val) + "->")
        return left + right
        

        