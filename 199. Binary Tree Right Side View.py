'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []

        def _rightSideView(root, depth=0):
            if root == None:
                return
            if len(output) == depth:
                output.append(root.val)
            _rightSideView(root.right, depth+1)
            _rightSideView(root.left, depth+1)

        _rightSideView(root)
        return output