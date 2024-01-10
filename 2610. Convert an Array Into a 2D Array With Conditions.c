/*
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
*/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findMatrix(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    // count num frequency (0-200)
    int dict[201] = {0};
    for(int i = 0; i < numsSize; i++){
        dict[nums[i]]++;
    }

    // calculate height of output matrix
    int m = dict[0];
    for(int i = 1; i < sizeof(dict)/sizeof(dict[0]); i++){
        if(dict[i] > m){
            m = dict[i];
        }
    }

    // allocate matrix array of rows
    *returnSize = m;// no. of rows (m)
    int** output = (int**)malloc(sizeof(int*)*returnSize[0]);
    
    // allocate each rows buffer
    *returnColumnSizes = (int*)malloc(sizeof(int)*returnSize[0]);
    for(int i = 0; i < m; i++){
        returnColumnSizes[0][i] = 200;
        output[i] = (int*)malloc(sizeof(int)*200);
    }

    // for each row
    for(int i = 0; i < m; i++){
        returnColumnSizes[0][i] = 0;
        // move 1 from each element in dict into the row and decrement dict[n]
        for(int j = 0; j < sizeof(dict)/sizeof(dict[0]); j++){
            if(dict[j] > 0){
                output[i][returnColumnSizes[0][i]++] = j;
                dict[j]--;
            } 
        }
    }
    return output;
}