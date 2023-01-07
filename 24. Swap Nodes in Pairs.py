'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head, tail=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """             
        if head and head.next:        
            temp = head.next# 2         
            head.next = head.next.next# 1.next = 3
            temp.next = head# 2.next = 1
            # 2 -> 1 -> 3
            if tail:
                tail.next = temp
            self.swapPairs(head.next, head)
            return temp
        return head
        