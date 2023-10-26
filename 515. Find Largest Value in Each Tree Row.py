'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        def _largestValues(node, depth=0):
            # base case 
            if node == None:
                return
            
            # save max value for each depth into an output arr
            if len(output) == depth:
                output.append(node.val)
            else:
                output[depth] = max(output[depth], node.val)

            # traversal
            _largestValues(node.left, depth+1)
            _largestValues(node.right, depth+1)

        _largestValues(root)
        return output
        