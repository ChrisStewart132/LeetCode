/*
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** mat, int matSize, int* matColSize, int* returnSize) {
    *returnSize = matSize * matColSize[0];
    int* output = malloc(sizeof(int) * returnSize[0]);

    int i = 0;
    int j = 0;
    int n = 0;
    bool up = true;
    while(n < returnSize[0]){
        //printf("%d,%d\n", i, j);
        output[n++] = mat[i][j];
        if(up){
            if(i==0 && j==matColSize[i]-1){
                i++;
                up=!up;
            }else if(j==matColSize[i]-1){
                i++;
                up=!up;
            }else if(i==0){
                j++;
                up=!up;
            }else{
                i--;
                j++;
            }
        }else{
            if(j==matColSize[i]-1 && i==matSize-1){
                j++;
                up=!up;
            }else if(i==matSize-1){
                j++;
                up=!up;
            }else if(j==0){
                i++;
                up=!up;
            }else{
                i++;
                j--;
            }
        }
    }

    return output;
}