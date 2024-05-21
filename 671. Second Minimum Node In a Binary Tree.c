/**
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 void _selection_sort(int* arr, int n) {
    int minIndex;
    for (int i = 0; i < n - 1; i++) {
        minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}
 void _dfs(struct TreeNode* root, int* cache, int* i) {
    if(root == NULL){
        return;
    }
    _dfs(root->left, cache, i);
    _dfs(root->right, cache, i);
    cache[(*i)++] = root->val;
}
int findSecondMinimumValue(struct TreeNode* root) {
    int cache[25] = {0};
    int length = 0;
    _dfs(root, cache, &length);// convert tree to arr
    _selection_sort(cache, length);
    int smallest = cache[0];
    int output = -1;
    for(int i = 0; i < length && output==-1; i++){
        output = cache[i] != smallest ? cache[i] : output;
    }
    return output;
}   