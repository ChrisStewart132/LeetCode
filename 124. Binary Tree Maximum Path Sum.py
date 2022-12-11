'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cache = {}
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:# base case
            return -1001
        
        # traverse down tree
        self.maxPathSum(root.left)
        self.maxPathSum(root.right)
        
        # either path left+self+up, right+self+up, left+self+right, left, right, self
        # cache the two options
            # 'c' closed: complete path 
            # 'o' open: in-complete path that can be extended  
        left = self.cache[(root.left, 'o')] if (root.left, 'o') in self.cache else -1001# -1001 as lowest possible val == -1000 (e.g. -1001 = -inf)
        right = self.cache[(root.right, 'o')] if (root.right, 'o') in self.cache else -1001
        left_c = self.cache[(root.left, 'c')] if (root.left, 'c') in self.cache else -1001
        right_c = self.cache[(root.right, 'c')] if (root.right, 'c') in self.cache else -1001
        self.cache[(root, 'c')] = max(left+right+root.val, left, right, left_c, right_c)
        self.cache[(root, 'o')] = max(left+root.val, right+root.val, root.val)
        x, y = self.cache[(root, 'o')], self.cache[(root, 'c')]
        #print(root.val, x,y, max(x,y))
        return max(x,y)
        