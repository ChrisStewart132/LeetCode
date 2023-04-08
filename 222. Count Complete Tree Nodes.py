# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        def right_depth(root):     
            return 0 if root == None else 1 + right_depth(root.right)

        rd = right_depth(root)

        def count_leaves(root, depth=0):
            if depth < rd-1:# traverse to rd
                left = count_leaves(root.left, depth+1)
                right = count_leaves(root.right, depth+1)
            elif depth == rd-1:# lowest full depth (rd)
                left = count_leaves(root.left, depth+1)
                if left == 0:
                    return 0
                right = count_leaves(root.right, depth+1)
                if right == 0:
                    return left
            else:# leaves
                return 1 if root else 0
            return left+right

        return sum([2**i for i in range(rd)]) + count_leaves(root)
