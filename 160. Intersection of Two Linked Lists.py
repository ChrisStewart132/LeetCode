'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object): 
    def getIntersectionNode(self, headA, headB, s=None):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not s:
            s = set()

        if not headA and not headB:
            return None
        
        if headA:    
            if headA in s:
                return headA
            s.add(headA)
            headA = headA.next
                
        if headB:     
            if headB in s:
                return headB
            s.add(headB)
            headB = headB.next   
        
        return self.getIntersectionNode(headA, headB, s)
              
