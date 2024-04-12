/*
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

    Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
    Now, first Bob will append the removed element in the array arr, and then Alice does the same.
    The game continues until nums becomes empty.

Return the resulting array arr.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void insertion_sort(int* nums, int numsSize){
     for(int i = 1; i < numsSize; i++){
         int j = i;
         int current = nums[j];
         while(j > 0 && nums[j-1] > current){
             nums[j] = nums[j-1];
             j--;
         }
         nums[j] = current;
     }
 }

int* numberGame(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* arr = (int*)malloc(sizeof(int)*returnSize[0]);
    insertion_sort(nums, numsSize);
    for(int i = 0; i < numsSize; i+=2){
        arr[i] = nums[i+1];
        arr[i+1] = nums[i];
    }
    return arr;
}