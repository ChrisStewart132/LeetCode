/*
You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k.
*/
int minOperations(int* nums, int numsSize, int k){
    int total = k*(k+1)/2;
    int* cache = calloc(sizeof(int), (k+1));
    int nOperations = 0;
    for(int i = numsSize-1; i > -1 && total > 0; i--){
        //printf("%d\n", nums[i]);
        if(nums[i] <= k && cache[nums[i]] == 0){
            total -= nums[i];
            cache[nums[i]] = 1;
        }
        nOperations++;
    }
    free(cache);
    return nOperations;
}