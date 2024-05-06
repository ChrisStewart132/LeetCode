/*
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* _removeNodes(struct ListNode* head, struct ListNode* prev, int* max_ptr) {
    if(head == NULL){
        return NULL;
    }

    // traverse right
    _removeNodes(head->next, head, max_ptr);
    
    if(*max_ptr > head->val){// remove current node
        if(prev == NULL){
            return head->next;
        }
        prev->next = head->next;
    }else{
        *max_ptr = head->val;
    }
    return head;
}

struct ListNode* removeNodes(struct ListNode* head) {
    int max = -1;
    return _removeNodes(head, NULL, &max);
}