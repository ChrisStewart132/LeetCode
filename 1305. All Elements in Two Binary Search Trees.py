# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, root):
        if root == None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def merge_sorted_lists(self, list1, list2):
        merged_list = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        merged_list += list1[i:]
        merged_list += list2[j:]
        return merged_list

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        return self.merge_sorted_lists(self.inOrder(root1), self.inOrder(root2))
