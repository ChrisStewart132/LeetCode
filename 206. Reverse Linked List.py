'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return prev

        tail = self.reverseList(head.next, head)  
        head.next = prev
        return tail