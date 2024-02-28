'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    depth = -1
    val = None
    def findBottomLeftValue(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:# base case
            return
        if root.left == None and depth > self.depth:# save the deepest left node
            self.depth, self.val = depth, root.val
        # dfs traversal 
        self.findBottomLeftValue(root.left, depth+1)
        self.findBottomLeftValue(root.right, depth+1)
        return self.val
        