/*
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int targetSum) {
    if(!root){
        return false;
    }else if(targetSum == root->val && !root->left && !root->right){
        return true;
    }
    bool l = false;
    bool r = false;
    targetSum -= root->val;
    if(root->left){
        l = hasPathSum(root->left, targetSum);
    }
    if(root->right){
        r = hasPathSum(root->right, targetSum);
    } 
    return l || r;
}