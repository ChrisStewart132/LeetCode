'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
 (i.e., from left to right, level by level from leaf to root).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def levelOrderBottom(self, root, depth=1, output=None):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # setup the 2d output which requires knowing the maximum depth of the tree O(n)
        if output == None:
            self.max_depth = self.maxDepth(root)
            output = [[] for i in range(self.max_depth)]
            #print(self.max_depth, output)
        if root == None:
            return
        # dfs O(n)
        self.levelOrderBottom(root.left, depth+1, output)
        self.levelOrderBottom(root.right, depth+1, output)
        output[self.max_depth-depth].append(root.val)
        return output