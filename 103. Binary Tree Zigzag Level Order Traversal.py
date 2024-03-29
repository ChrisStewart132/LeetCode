'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        def _zigzagLevelOrder(root, depth=0):
            if root == None:
                return
            
            while len(output) <= depth:
                output.append([])
            output[depth].append(root.val)

            _zigzagLevelOrder(root.left, depth+1)
            _zigzagLevelOrder(root.right, depth+1)

        _zigzagLevelOrder(root)
        for i in range(1, len(output), 2):
            output[i].reverse()
        return output