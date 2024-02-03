/*
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int rangeSumBST(struct TreeNode* root, int low, int high) {
    if(root == NULL){
        return 0;
    }
    int total = 0;
    if(root->val <= high && root->val >= low){// in range, add and search left+right
        total += root->val;
        total += rangeSumBST(root->right, low, high);
        total += rangeSumBST(root->left, low, high);
    }else if(root->val < low){// search right
        total += rangeSumBST(root->right, low, high);
    }else {// search left
        total += rangeSumBST(root->left, low, high);
    }
    return total;
}