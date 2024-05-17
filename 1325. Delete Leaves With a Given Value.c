/*
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, 
if its parent node becomes a leaf node and has the value target, 
it should also be deleted (you need to continue doing that until you cannot).
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* _removeLeafNodes(struct TreeNode* root, int target, int depth) {
    if(root == NULL){
        return NULL;
    }
    int l = _removeLeafNodes(root->left, target, depth+1);
    int r = _removeLeafNodes(root->right, target, depth+1);
    if(l==1){
        root->left = NULL;
    }
    if(r==1){
        root->right = NULL;
    }
    // leaf target
    if(root->left == NULL && root->right == NULL && root->val == target){
        return depth == 0 ? NULL : 1;
    }
    return root;
}

struct TreeNode* removeLeafNodes(struct TreeNode* root, int target) {
    return _removeLeafNodes(root, target, 0);
}