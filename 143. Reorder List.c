/*
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int len(struct ListNode* head){
    if(head == NULL){
        return 0;
    }
    return 1 + len(head->next);
}
void reorderList(struct ListNode* head) {
    int length = len(head);
    struct ListNode** cache = malloc(sizeof(struct ListNode*) * length);
    struct ListNode** cache2 = malloc(sizeof(struct ListNode*) * length);
    struct ListNode* temp = head;
    for(int i = 0; i < length; i++){
        cache[i] = temp;
        temp = temp->next;
        //printf("%d\n", cache[i]->val);
    }
    for(int i = 0; i < length; i++){
        if(i%2 == 0){
            cache2[i] = cache[i/2];
        }else{
            cache2[i] = cache[length-1-i/2];
        }   
    }
    for(int i = 1; i < length; i++){
        cache2[i-1]->next = cache2[i];
        //printf("i:%d v:%d\n", i, cache2[i]->val);
    }
    cache2[length-1]->next = NULL;
    free(cache);
    free(cache2);
}