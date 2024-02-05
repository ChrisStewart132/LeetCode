'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def _search(root, x, depth=0, parent=None):
            if root == None:
                return
            if x == root.val:
                return depth, parent
            l = _search(root.left, x, depth+1, root)
            r = _search(root.right, x, depth+1, root)
            return l if l else r

        dx, px = _search(root, x)
        dy, py = _search(root, y)

        return dx==dy and px!=py