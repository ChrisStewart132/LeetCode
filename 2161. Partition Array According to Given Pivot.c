/*
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

    Every element less than pivot appears before every element greater than pivot.
    Every element equal to pivot appears in between the elements less than and greater than pivot.
    The relative order of the elements less than pivot and the elements greater than pivot is maintained.
        More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.

Return nums after the rearrangement.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int l = 0;// nLess
    int r = 0;// nGreater
    int m = 0;// nPivots
    for(int i = 0;i < numsSize; i++){
        if(nums[i] < pivot){
            l++;
        }else if(nums[i] == pivot){
            m++;
        }else{
            r++;
        }
    }
    int* left = (int*)malloc(sizeof(int)*l);
    int* right = (int*)malloc(sizeof(int)*r);
    l = 0;
    r = 0;
    for(int i = 0;i < numsSize; i++){
        if(nums[i] < pivot){
            left[l++] = nums[i];
        }else if(nums[i] > pivot){
            right[r++] = nums[i];
        }
    }
    for(int i = 0; i < l; i++){
        nums[i] = left[i];
    }
    for(int i = 0; i < m; i++){
        nums[i+l] = pivot;
    }
    for(int i = 0; i < r; i++){
        nums[l+m+i] = right[i];
    }
    free(left);
    free(right);
    *returnSize = numsSize;
    return nums;
}