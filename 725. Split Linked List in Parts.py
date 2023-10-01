'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        output = [head]
        def _len(head):
            return 1 + _len(head.next) if head else 0
        l = _len(head)

        current, previous, i = head, None, 0
        r = l%k if l > k else 0
        while current:
            #print(len(output), i, max(1, l//k + min(1,r)))
            if i == max(1, l//k + min(1,r)):# split
                r = r-1 if r > 0 else 0# decrement remainder for lists with 1 extra node
                output += [current]# add the start of the next linked list
                previous.next = None# cut the link
                i = 0
            previous, current, i = current, current.next, i+1

        return output + [None for i in range(len(output), k)]

        