'''
A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeByLevel(self, root, output, depth=0):
        if root == None:
            return
        if len(output) <= depth:
            output.append([])
        output[depth].append(root.val)
        self.treeByLevel(root.left, output, depth+1)
        self.treeByLevel(root.right, output, depth+1)
    def checkLevel(self, arr, depth=0):
        if arr[0]%2 == depth%2:
            return False
        for i in range(1, len(arr)):
            if arr[i]%2 == depth%2:
                return False
            if depth%2==0 and arr[i-1] >= arr[i]:
                return False
            elif depth%2==1 and arr[i-1] <= arr[i]:
                return False
        return True
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        levels = []
        self.treeByLevel(root, levels)
        return all([self.checkLevel(arr, depth) for depth, arr in enumerate(levels)])