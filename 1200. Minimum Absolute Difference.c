'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

'''
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void countingSort(int* nums, int numsSize, int min, int max){
    // create a buffer of max-min+1 length
    int* buffer = (int*)calloc((max-min+1), sizeof(nums[0]));
    // key=n-min and buffer[key] = count of n in nums
    for(int i = 0;i < numsSize; i++){
        buffer[nums[i]-min] += 1;
    }
    // re-write nums given the order and counts of each n
    int j = 0;
    for(int i = 0; i < (max-min+1); i++){
        while(buffer[i] > 0){
            nums[j] = min+i;
            buffer[i]--;
            j++;
        }
    }
    free(buffer);
}

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) { 
    // counting sort in place the arr
    int max = arr[0];
    int min = max;
    for(int i = 1; i < arrSize; i++){
        max = arr[i]>max?arr[i]:max;
        min = arr[i]<min?arr[i]:min;
    }
    countingSort(arr, arrSize, min, max);
    
    // calculate the min-dist
    int d = arr[1]-arr[0];
    for(int i = 2; i < arrSize; i++){
        if(arr[i]-arr[i-1] < d){
            d = arr[i]-arr[i-1];
        }
    }
    
    // calculate the number of pairs
    (*returnSize) = 0;
    for(int i = 1; i < arrSize; i++){
        if(arr[i]-arr[i-1] == d){
            (*returnSize)++;// increment the output size
        }
    }
    
    //printf("d:%d, n:%d\n", d, *returnSize);
    
    // allocate the output buffer
    int** output = (int**)malloc(sizeof(int*)*(*returnSize));
    *returnColumnSizes = (int*)malloc(sizeof(int) * (*returnSize));
    for (int i = 0; i < *returnSize; ++i) {
        output[i] = (int*)malloc(sizeof(int) * 2);
        (*returnColumnSizes)[i] = 2;  // Each column size is 2
    }
    
    // set the pairs in output
    int j = 0;
    for(int i = 1; i < arrSize; i++){
        if(arr[i]-arr[i-1] == d){
            int* pair = (int*)malloc(2*sizeof(int));
            pair[0] = arr[i-1];
            pair[1] = arr[i];
            output[j++] = pair;
        }
    }                     
    return output;
}