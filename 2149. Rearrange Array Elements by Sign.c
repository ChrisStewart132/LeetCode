/*
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int* positive = (int*)malloc(sizeof(int)*numsSize/2);
    int* negative = (int*)malloc(sizeof(int)*numsSize/2);
    int p = 0;
    int n = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] < 0){
            negative[n++] = nums[i];
        }else{
            positive[p++] = nums[i];
        }
    }
    p = 0;
    n = 0;
    for(int i = 0; i < numsSize; i+=2){
        nums[i] = positive[p++];
        nums[i+1] = negative[n++];
    }
    free(positive);
    free(negative);
    *returnSize = numsSize;
    return nums;
}