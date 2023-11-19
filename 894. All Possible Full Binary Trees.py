'''
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    cache = None
    #def tree_len(self, root):
        #return 1 + self.tree_len(root.left) + self.tree_len(root.right) if root else 0

    def serialize_tree(self, root, depth=0, width=0):
        if not root:
            return ()
        return ((depth, width),) + self.serialize_tree(root.left, depth+1, width-1) + self.serialize_tree(root.right, depth+1, width+1)


    def leaf_nodes(self, root):
        if root is None:
            return []
        if root.left == None == root.right:  # Check if it's a leaf node
            return [root]
        return self.leaf_nodes(root.left) + self.leaf_nodes(root.right)

    def copy_tree(self, root):
        if root is None:
            return None
        copy = TreeNode(root.val)
        copy.left = self.copy_tree(root.left)
        copy.right = self.copy_tree(root.right)
        return copy

    def trees_equal(self, a, b):
        if a == b == None:
            return True
        elif a == None or b == None:
            return False
        return self.trees_equal(a.left, b.left) and self.trees_equal(a.right, b.right)

    def is_solution(self, candidate, n, output, length):
        return length == n #and all([not(self.trees_equal(candidate, x)) for x in output])
        '''if length == n:
            for x in output:
                if self.trees_equal(candidate, x):
                    return False
        return False'''

    def children(self, candidate, n, length, leaf_nodes):
        output = []
        #length = self.tree_len(candidate)
        if length < n:
            #leaf_nodes = self.leaf_nodes(candidate)
            for leaf in leaf_nodes:
                leaf.right, leaf.left = TreeNode(0), TreeNode(0)
                serialized_tree = self.serialize_tree(candidate)
                if serialized_tree not in self.cache:
                    self.cache.add(serialized_tree)
                    output.append(self.copy_tree(candidate))# copy the modified tree
                leaf.right, leaf.left = None, None  # Reset 

        return output

    def dfs_backtrack(self, n, output, is_solution, children, candidate, length):
        """
        output: container solutions are added to
        is_solution: boolean function, true if candidate is a solution
        children: function that returns child nodes/variant of the given node/candidate
        """
        if is_solution(candidate, n, output, length):
            output.append(self.copy_tree(candidate))
        else:
            for child_candidate in children(candidate, n, length, self.leaf_nodes(candidate)):
                self.dfs_backtrack(n, output, is_solution, children, child_candidate, length+2)

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 1:
            return [TreeNode()]

        if n % 2 == 0:# all full binary trees are odd
            return []

        self.cache = set()

        output = []
        self.dfs_backtrack(n, output, self.is_solution, self.children, TreeNode(), 1)
        return output

        