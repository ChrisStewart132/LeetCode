'''
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

    For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].

Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def reverseOddLevels(self, l, r=None, depth=0):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if l == None:
            return

        if depth == 0:
            self.reverseOddLevels(l.left, l.right, depth+1)
            return l

        if depth % 2 == 1:
            l.val, r.val = r.val, l.val

        self.reverseOddLevels(l.left, r.right, depth+1)
        self.reverseOddLevels(l.right, r.left, depth+1)         