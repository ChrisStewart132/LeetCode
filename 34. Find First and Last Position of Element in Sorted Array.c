/*
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 
 [-3,-2,-1]
0
[2,2]
2
[5,7,7,8,8,10]
8
[8]
8
[1]
8
[5,7,7,8,8,10]
6
[5,7,7,8,8,10]
7
[5,7,7,8,8,10]
8
[5,7,7,8,8,10]
5
[5,7,7,8,8,10]
10
 */
int searchFirst(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize-1;
    while(l+1 < r){
        int m = l+((r-l)>>1);
        if(nums[m] < target){// check right of m
            l=m+1;
        }else{// target or left of m
            r=m;
        }
    }
    if(nums[l] == target){
        return l;
    }
    if(nums[r] == target){
        return r;
    }
    return -1;
}

int searchLast(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize-1;
    while(l < r-1){
        int m = l+((r-l)>>1);
        if(nums[m] > target){
            r=m-1;
        }else{
            l=m;
        }
    }
    printf("%d %d", numsSize, r);
    if(nums[r] == target){
        return r;
    }
    if(nums[l] == target){
        return l;
    }
    return -1;
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* range = malloc(sizeof(int)*2);
    if(numsSize == 1){
        range[0] = nums[0] == target?0:-1;
        range[1] = nums[0] == target?0:-1;
    } else if(numsSize == 0){
        range[0] = -1;
        range[1] = -1;
    }else{
        range[0] = searchFirst(nums, numsSize, target);
        range[1] = searchLast(nums, numsSize, target);
    }  
    return range;
}