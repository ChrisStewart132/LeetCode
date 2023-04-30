'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
binary search tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            m = len(nums)//2
            return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), self.sortedArrayToBST(nums[m+1:]))
