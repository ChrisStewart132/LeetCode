'''
Given a binary tree with the following rules:

    root.val == 0
    If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
    If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

    FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
    bool find(int target) Returns true if the target value exists in the recovered binary tree.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.values = set()
        self._build(root)

    def _build(self, root, value=0):
        if root == None:
            return
        self.values.add(value)
        root.val = value

        self._build(root.left, 2*value+1)
        self._build(root.right, 2*value+2)


    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)