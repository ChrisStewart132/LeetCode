//Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool _isSymmetric(struct TreeNode* l, struct TreeNode* r) {
    if(!l && !r){
        return true;
    }else if(l && r){
        return l->val == r->val && _isSymmetric(l->left, r->right) && _isSymmetric(l->right, r->left);
    }
    return false;
}

bool isSymmetric(struct TreeNode* root) {
    return root && _isSymmetric(root->left, root->right);
}