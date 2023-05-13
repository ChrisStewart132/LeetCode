'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root, i=0, output=None):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return 
        if output == None:
            output = []
        if len(output) == i:
            output.append((0,0))
        
        output[i] = output[i][0] + root.val, output[i][1] + 1
        self.averageOfLevels(root.left, i+1, output)
        self.averageOfLevels(root.right, i+1, output)
        return [float(x)/y for x,y in output]
        

        