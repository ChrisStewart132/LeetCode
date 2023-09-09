'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output, r = [], 0
        while l1 and l2:
            output.append(l1.val + l2.val + r)
            if output[-1] > 9:
                output[-1], r = output[-1]-10, 1
            else:
                r = 0
            l1, l2 = l1.next, l2.next

        tail = l1 if l1 else l2
        while tail:
            output.append(tail.val + r)
            if output[-1] > 9:
                output[-1], r = output[-1]-10, 1
            else:
                r = 0
            tail = tail.next

        if r == 1:
            output.append(1)

        # convert stack to a linked list, simple but less optimal
        head = ListNode(output[0])
        current = head
        for i in range(1, len(output)):
            current.next = ListNode(output[i])
            current = current.next

        return head
            
        
        

