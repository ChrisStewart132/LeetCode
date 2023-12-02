'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root, prev=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inOrder(root):
            if root == None:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)

        arr = inOrder(root)
        ans = abs(arr[1]-arr[0])
        for i in range(2, len(arr)):
            ans=min(ans, abs(arr[i]-arr[i-1]))

        return ans
