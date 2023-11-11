'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        s1, s2, h = [], [], head
        while head != None:
            if head.val < x:
                s1.append(head.val)
            else:
                s2.append(head.val)
            head = head.next
        
        head = h
        for i in range(len(s1)):
            head.val = s1[i]
            head = head.next
        for i in range(len(s2)):
            head.val = s2[i]
            head = head.next

        return h