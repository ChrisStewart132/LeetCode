/*
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int _sumOfLeftLeaves(struct TreeNode* root, int left) {
    if(!root){
        return 0;
    }
    int output = left == 1 && root->left == NULL && root->right == NULL? root->val : 0;
    output += _sumOfLeftLeaves(root->left, 1);
    output += _sumOfLeftLeaves(root->right, 0);
    return output;
}
int sumOfLeftLeaves(struct TreeNode* root) {
    return _sumOfLeftLeaves(root, 0);
}