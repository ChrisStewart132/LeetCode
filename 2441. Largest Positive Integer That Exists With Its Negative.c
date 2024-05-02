/*
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
*/
int findMaxK(int* nums, int numsSize) {
    int min = -1000;
    int cache[2001]={0};
    int output = -1;
    for(int i = 0; i < numsSize; i++){
        cache[nums[i]-min] = 1;
        if(cache[nums[i]*-1-min] == 1){
            output = abs(nums[i]) > output ? abs(nums[i]) : output;
        }
    }
    return output;
}