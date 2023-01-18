'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):   
    def __init__(self):
        self.head = None
        self.size = 0
      
    def getNode(self, index, head):
        """returns ith Node from the initial head_node given"""
        if index == 0 or head == None:
            return head
        return self.getNode(index-1, head.next)
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        return self.getNode(index, self.head).val if index < self.size else -1
    
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        h = Node(val)
        h.next = self.head
        self.head = h
        self.size += 1
        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head:
            tail = self.getNode(self.size-1, self.head)
            tail.next = Node(val)
            self.size += 1 
        else:
            self.addAtHead(val)
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > 0:
            prev = self.getNode(index-1, self.head)
            if prev:
                temp = prev.next
                prev.next = Node(val)
                prev.next.next = temp
                self.size += 1
        else:
            self.addAtHead(val)
        
    def deleteAtIndex(self, index):
        """        
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        elif self.size > index > -1:
            prev = self.getNode(index-1, self.head)
            prev.next = prev.next.next
            self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)