/*
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
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

int searchLeft(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize-1;
    while(l+1 < r){
        int m = (l+r)/2;
        if(nums[m] < target){
            l = m+1;
        }else{
            r = m;
        }
    }
    if(nums[l] == target){
        return l;
    } else if(l+1 < numsSize && nums[l+1] == target){
        return l+1;
    }
    return -1;
}

int searchRight(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize-1;
    while(l < r-1){
        int m = (l+r)/2;
        if(nums[m] > target){
            r = m-1;
        }else{
            l = m;
        }
    }
    if(l+1<numsSize && nums[l+1] == target){
        return l+1;
    } else if(l > -1 && nums[l] == target){
        return l;
    }
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    if(numsSize == 1){// base case
        if(nums[0] == target){       
            *returnSize = 1;  
            int* output = malloc(sizeof(int));
            *output = 0;
            return output;
        }else{
            *returnSize = 0;  
            return 0;
        }
    }
    countingSort(nums, numsSize, 1, 100);
    
    int l = searchLeft(nums, numsSize, target);
    if(l == -1){// target doesn't exist
        *returnSize = 0;  
        return 0;
    }
    int r = searchRight(nums, numsSize, target);
    
    // return the range of indices
    *returnSize = 1+r-l;
    int* output = (int*)malloc(sizeof(int)*returnSize[0]);
    for(int i = l; i <= r; i++){
        output[i-l] = i;
    }
    return output;
}