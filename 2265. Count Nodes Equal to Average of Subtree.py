'''
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cache = {None:(0,0)}
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        l = self.averageOfSubtree(root.left)
        r = self.averageOfSubtree(root.right)

        s = self.cache[root.left][0] + self.cache[root.right][0] + root.val
        n = self.cache[root.left][1] + self.cache[root.right][1] + 1
        self.cache[root] = (s, n)

        return l + r + 1 if s/n == root.val else l + r