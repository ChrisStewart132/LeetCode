'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head, prev=None, even_head=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            if prev:# last node in list is odd, need to set previous even node to null
                prev.next = None
            if head:# when odd is at end of list append even list to end
                head.next = even_head
            return head

        

        #print(head.val)
        odd = head# head of odd list
        even = head.next# head of even list
        if prev:
            prev.next = odd.next
        
        odd.next = odd.next.next  

        if even_head == None:
            even_head = even
                
        if odd.next == None:
            head.next = even_head
        else:
            self.oddEvenList(odd.next, even, even_head)

        # with 2*0(n) speed
        '''if prev==None:
            tail = odd
            while tail.next:
                tail = tail.next
            tail.next = even'''
        return odd



