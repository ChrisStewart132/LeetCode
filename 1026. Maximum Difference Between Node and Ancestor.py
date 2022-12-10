'''Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cache = {}
    def maxChild(self, root):
        if root==None:
            return 0
        if (root.left, "max") in self.cache:
            left = self.cache[(root.left, "max")]
        else:
            left = self.maxChild(root.left)
            self.cache[(root.left, "max")] = left

        if (root.right, "max") in self.cache:
            right = self.cache[(root.right, "max")]
        else:
            right = self.maxChild(root.right)
            self.cache[(root.right, "max")] = right
        return max(root.val,left,right)

    def minChild(self, root):
        if root==None:
            return 10**6
        if (root.left, "min") in self.cache:
            left = self.cache[(root.left, "min")]
        else:
            left = self.minChild(root.left)
            self.cache[(root.left, "min")] = left

        if (root.right, "min") in self.cache:
            right = self.cache[(root.right, "min")]
        else:
            right = self.minChild(root.right)
            self.cache[(root.right, "min")] = right
        return min(root.val,left,right)

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        l,r = 0,0
        sl,lr = 0,0

        if root.left:
            if (root.left, 's') in self.cache:
                sl = self.cache[(root.left, 's')]
            else:
                sl = self.minChild(root.left)
                self.cache[(root.left, 's')] = sl

            if (root.left, 'l') in self.cache:
                ll = self.cache[(root.left, 'l')]
            else:
                ll = self.maxChild(root.left)
                self.cache[(root.left, 'l')] = ll
            l = max(abs(root.val - sl), abs(root.val - ll))

        if root.right:
            if (root.right, 'l') in self.cache:
                lr = self.cache[(root.right, 'l')]
            else:             
                lr = self.maxChild(root.right)
                self.cache[(root.right, 'l')] = lr

            if (root.right, 's') in self.cache:
                sr = self.cache[(root.right, 'l')]
            else:
                sr = self.minChild(root.right) 
                self.cache[(root.right, 'l')] = sr
            r =  max(abs(root.val - lr), abs(root.val - sr))

        n = max(l,r)
        al,ar = 0,0
        if root.left and root.left in self.cache:
            al = self.cache[root.left]
        elif root.left:
            al = self.maxAncestorDiff(root.left)
            self.cache[root.left] = al

        if root.right and root.right in self.cache:
            ar = self.cache[root.right]
        elif root.right:           
            ar = self.maxAncestorDiff(root.right)
            self.cache[root.right] = ar

        return max(n, al, ar)

        