/*
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int _sumNumbers(struct TreeNode* root, int* cache, int depth) {
    if(root == NULL){
        return 0;
    }
    cache[depth] = root->val;
    if(root->left == NULL && root->right == NULL){
        int total = 0;
        for(int i = 0; i <= depth; i++){
            total += cache[i] * pow(10, depth-i);
        }
        //printf("total:%d, val:%d\n", total, root->val);
        return total;
    }
    int l = _sumNumbers(root->left, cache, depth+1);
    int r = _sumNumbers(root->right, cache, depth+1);
    return l+r;
}
int sumNumbers(struct TreeNode* root) {
    int cache[10];// The depth of the tree will not exceed 10.
    return _sumNumbers(root, cache, 0);
}