/*
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
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
    // traverses the linked list entirely, caches it, and returns the middle element
    ListNode* middleNode(ListNode* head) {
        vector<ListNode*> l;
        ListNode* current = head;
        while(current != nullptr){
            l.push_back(current);
            current = current->next;
        }
        return l[(int)(l.size() / 2)];
    }
};