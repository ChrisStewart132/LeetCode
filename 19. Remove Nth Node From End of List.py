'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        if n == 1: # remove tail
            if len(stack) > 1:
                stack[-n-1].next = None
            else:
                return None
        elif n == len(stack): # remove head
            if len(stack) > 1:
                return stack[-n+1]
            else:
                return None
        else:
            stack[-n-1].next = stack[-n+1]
        return head