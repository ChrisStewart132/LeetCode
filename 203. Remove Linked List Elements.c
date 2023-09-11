/*
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    while(head != NULL && head->val == val) {// remove initial un-wanted nodes
        head = head->next;
    }
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    while(curr != NULL) {
        if(curr->val == val) {// remove node
            prev->next = curr->next;
        } else {
            prev = curr;
        }   
        curr = curr->next;
    }
    return head;
}