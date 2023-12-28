//Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int max(int a, int b){
    return a > b?a:b;
}
int min(int a, int b){
    return a < b?a:b;
}

int maxDepth(struct TreeNode* root, int depth){
    if(root){
        return 1 + max(maxDepth(root->left, depth+1), maxDepth(root->right, depth+1));
    }
    return 0;
}

void _levelOrder(struct TreeNode* root, int** output, int* returnColumnSizes, int depth){
    if(root){
        output[depth][returnColumnSizes[depth]++] = root->val;
        _levelOrder(root->left, output, returnColumnSizes, depth+1);
        _levelOrder(root->right, output, returnColumnSizes, depth+1);
    }
}

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    *returnSize = maxDepth(root, 0);
    //printf("%d max depth\n", returnSize[0]);
    int** output = malloc(sizeof(int*)*returnSize[0]);
    for(int i = 0; i < *returnSize; i++){
        // assume each depth has the maximum number of nodes
        int space = min((1<<min(i,11)), 2000);
        //printf("%d\n", space);
        output[i] = calloc(sizeof(int), space);// 1,2,4,8,16,32,64...2000
    }
    *returnColumnSizes = calloc(sizeof(int), returnSize[0]);
    _levelOrder(root, output, *returnColumnSizes, 0);
    return output;
    
}