/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
*/
int max(int a, int b){
    return a>b?a:b;
}

int rob(int* nums, int numsSize) {
    if(numsSize == 1){
        return nums[0];
    }
    if(numsSize == 2){
        return max(nums[0], nums[1]);
    }
    nums[numsSize-2] = max(nums[numsSize-1], nums[numsSize-2]);
    int output = nums[numsSize-2];
    for(int i = numsSize-3; i > -1; i--){
        nums[i] = max(nums[i+1], nums[i]+nums[i+2]);
        output = max(output, nums[i]);
    }
    return output;
}