/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // recursively traverses down 1 of the 2 linked lists, merging, and returning the head node from first call
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* output;
        if(!list2){
            return  list1;
        }
        if(!list1){
            return list2;
        }

        if(list1->val < list2->val){
            output = list1;
            output->next = mergeTwoLists(list1->next, list2);
        } else {
            output = list2;
            output->next = mergeTwoLists(list1, list2->next);
        }

        return output;
    }
};