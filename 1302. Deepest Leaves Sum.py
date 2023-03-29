# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_leaf(self, node):
        return node.left == node.right == None

    def tree_depth(self, root, depth=0):
        if root == None:
            return 0
        if self.is_leaf(root):
            return depth
        return max(self.tree_depth(root.left, depth+1), self.tree_depth(root.right, depth+1))

    def deepestLeavesSum(self, root):
        target_depth = self.tree_depth(root)
        def _deepestLeavesSum(root, depth=0):
            if root == None:
                return 0
            if self.is_leaf(root):
                return root.val if depth == target_depth else 0
            return _deepestLeavesSum(root.left, depth+1) + _deepestLeavesSum(root.right, depth+1)
        return _deepestLeavesSum(root)




        