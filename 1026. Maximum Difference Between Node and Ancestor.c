/*
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

 // compare current with the max and min of the currents ancestors/subtree nodes

# define INF 1000000
int min(int a, int b){
    return a<b?a:b;
}
int max(int a, int b){
    return a>b?a:b;
}
int min_node(struct TreeNode* root){
    if(root == NULL){
        return INF;
    }
    return min(root->val, min(min_node(root->left), min_node(root->right)));
}
int max_node(struct TreeNode* root){
    if(root == NULL){
        return 0;
    }
    return max(root->val, max(max_node(root->left), max_node(root->right)));
}

int maxAncestorDiff(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int left_min = root->val;
    int left_max = root->val;
    if(root->left){
        left_min = min_node(root->left);
        left_max = max_node(root->left);
    }
    int right_min = root->val;
    int right_max = root->val;
    if(root->right){
        right_min = min_node(root->right);
        right_max = max_node(root->right);
    }
    int smallest = min(left_min, right_min);
    int largest = max(left_max, right_max);
    int diff = max(abs(smallest-root->val), abs(largest-root->val));

    return max(diff, max(maxAncestorDiff(root->left), maxAncestorDiff(root->right)));    
}