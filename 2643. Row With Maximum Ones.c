/*
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int count(int* row, int n, int val){
    int c = 0;
    for(int i = 0; i < n; i++){
        if(row[i] == val){
            c++;
        }
    }
    return c;
}

int* rowAndMaximumOnes(int** mat, int matSize, int* matColSize, int* returnSize){
    *returnSize = 2;
    int* output = (int*)malloc(sizeof(int)*returnSize[0]);
    output[0] = 0;
    output[1] = count(mat[0], matColSize[0], 1);
    for(int i = 1; i < matSize; i++){
        int nOnes = count(mat[i], matColSize[i], 1);
        if(nOnes > output[1]){
            output[0] = i;
            output[1] = nOnes;
        }
    }
    return output;
}