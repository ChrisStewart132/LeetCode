'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        def _levelOrder(root, depth=0):
            if root == None:
                return

            while len(output) <= depth:
                output.append([])
            output[depth].append(root.val)

            _levelOrder(root.left, depth+1)
            _levelOrder(root.right, depth+1)
            
        _levelOrder(root)
        return output