/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool _isValidBST(struct TreeNode* root, int64_t min, int64_t max) {
    if(!root){
        return true;
    }
    return root->val>min && root->val<max && _isValidBST(root->left, min, root->val) && _isValidBST(root->right, root->val, max);
}

bool isValidBST(struct TreeNode* root) {
    if(!root){
        return true;
    }
    int64_t max = INT64_MAX;
    int64_t min = INT64_MIN;
    return _isValidBST(root, min, max);
}