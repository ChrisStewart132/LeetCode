'''
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    largest = -1
    def removeNodes(self, head, prev=None):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return
        # traverse right
        self.removeNodes(head.next, head)
        if self.largest > head.val:# remove current node
            if prev == None:
                return head.next
            prev.next = head.next
        else:
            self.largest = head.val
        return head


        