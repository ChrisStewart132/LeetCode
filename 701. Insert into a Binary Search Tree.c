/*
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void _insertIntoBST(struct TreeNode* root, struct TreeNode* parent, int val) {
    if(!root){
        struct TreeNode* node = calloc(sizeof(struct TreeNode), 1);
        node->val = val;
        if(val < parent->val){
            parent->left = node;
        }else{
            parent->right = node;
        }
    }else if(val < root->val){
        _insertIntoBST(root->left, root, val);
    }else{
        _insertIntoBST(root->right, root, val);
    }
}

struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    if(!root){
        root = calloc(sizeof(struct TreeNode), 1);
        root->val = val;  
    }else{
        _insertIntoBST(root, root, val);
    }
    return root;
}