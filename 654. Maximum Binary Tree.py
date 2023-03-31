# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            i = nums.index(max(nums))
            left, right = nums[:i], nums[i+1:]
            return TreeNode(nums[i], self.constructMaximumBinaryTree(left), self.constructMaximumBinaryTree(right))