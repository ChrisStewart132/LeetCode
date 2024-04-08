'''
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

    The height of the tree is height and the number of rows m should be equal to height + 1.
    The number of columns n should be equal to 2height+1 - 1.
    Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
    For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
    Continue this process until all the nodes in the tree have been placed.
    Any empty cells should contain the empty string "".

Return the constructed matrix res.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def max_depth(self, root):
        if root == None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    def build_tree_matrix(self, root, output, i, j):
        if root == None:
            return
        output[i][j] = str(root.val)
        x = 2**(len(output)-i-2)
        self.build_tree_matrix(root.left, output, i+1, j-x)
        self.build_tree_matrix(root.right, output, i+1, j+x)
        
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        max_depth = self.max_depth(root)
        m = max_depth
        n = sum([2**i for i in range(max_depth)])# the width (n) must have space for all nodes in the binary tree
        output = [["" for i in range(n)] for j in range(m)]
        i,j = 0, (n-1)/2
        self.build_tree_matrix(root, output, i, j)
        return output