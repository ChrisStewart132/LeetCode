/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ListNode* temp = head;
        while(temp){
            length++;
            temp = temp->next;
        }
        std::cout<<length<<std::endl;

        // remove head base case as n >= 1 and ListNode_length >= 1
        if(length == n){
            return head->next;
        }

        temp = head;
        ListNode* prev = NULL;
        // traverse temp to the node to remove, and prev to the previous node
        for(int i = 0; i < length-n; i++){
            prev = temp;
            temp = temp->next;
        }
        std::cout << prev->val << std::endl;
        // remove temp from the list
        prev->next = temp->next;

        return head;
    }
};