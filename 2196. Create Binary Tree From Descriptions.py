'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

    If isLefti == 1, then childi is the left child of parenti.
    If isLefti == 0, then childi is the right child of parenti.

Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        cache = {}# value -> TreeNodePtr
        children, parents = set(), set()
        for parent, child, isLeft in descriptions:
            children.add(child)
            parents.add(parent)

            if parent not in cache:
                cache[parent] = TreeNode(parent)
            if child not in cache:
                cache[child] = TreeNode(child)

            if isLeft:
                cache[parent].left = cache[child]
            else:
                cache[parent].right = cache[child]
                
        return cache[parents.difference(children).pop()]