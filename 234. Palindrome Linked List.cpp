//Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
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
    bool isPalindrome(ListNode* head) {
        std::vector<int> list;
        for(const ListNode* node = head; node != nullptr; node = node->next){
            list.push_back(node->val);
        }
        for(int i = 0; i < list.size()/2; i++){
            if(list[i] != list[list.size()-1-i]){
                return false;
            }
        }
        return true;
    }
};